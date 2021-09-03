
function inRad(num) {
    return num * Math.PI / 180;
}

// elementary drawers
class CanvasDrawer {
    constructor(strokeColor, strokeWidth, canvasCTX, coordinates) {
        this.strokeColor = strokeColor;
        this.canvasCTX = canvasCTX;
        this.strokeWidth = strokeWidth;
        this.coordinates = coordinates
        this.drawObject();
    }
    setContext() {
        if (this.strokeWidth) {
            this.canvasCTX.strokeStyle = this.strokeColor;
        }
        if (this.strokeColor) {
            this.canvasCTX.lineWidth = this.strokeWidth;
        }
    }
    drawObject() {
        this.setContext()
        this.canvasCTX.beginPath()
        for (let i in this.coordinates) {
            if (!i) {
                this.canvasCTX.moveTo(...this.coordinates[i])
            } else {
                this.canvasCTX.lineTo(...this.coordinates[i])
            }
            i++;
        }
        this.canvasCTX.stroke()
        this.canvasCTX.closePath()
        this.setContextDefault()
    }
    setContextDefault() {
        if (this.strokeWidth) {
            this.canvasCTX.strokeStyle = "#000000";
        }
        if (this.strokeColor) {
            this.canvasCTX.lineWidth = 1;
        }
    }
}

class CanvasTextBlock {
    constructor(text, text_font, coordinates, canvasCTX) {
        this.text_font = text_font 
        this.text = text
        this.coordinates = coordinates
        this.canvasCTX = canvasCTX
        this.drawObject()
    }
    drawObject() {
        this.canvasCTX.font = this.text_font; //'20px sans-serif';
        this.canvasCTX.textBaseline = "middle";
        this.canvasCTX.textAlign = "center";
        this.canvasCTX.fillText(this.text, ...this.coordinates);
    }
}

// drawers objects
class CanvasObjectDrawer {
    constructor(object, canvasCTX) {
        new CanvasDrawer(object.strokeColor, object.lineWidth, canvasCTX, object.all_coordinates)
    }
}

class CanvasTextDrawer {
    constructor(text_block, canvasCTX) {
        new CanvasTextBlock(text_block.text, text_block.font, text_block.all_coordinates, canvasCTX)
    }
}


// composition draw
class CanvasCompositionDrawer {
    constructor(allObjectsToDraw, canvasCTX) {
        this.allObjectsToDraw = allObjectsToDraw;
        this.canvasCTX = canvasCTX;
        this.pefromDraw();
    }
    pefromDraw() {
        for (let object of this.allObjectsToDraw) {
            this.drawObject(object)
        }
    }
    drawObject(inputObject) {
        if ("all_objects" in inputObject) {
            for (let object of inputObject.all_objects) {
                this.drawObject(object);
            }
        }
        if ("all_coordinates" in inputObject) {
            new CanvasObjectDrawer(inputObject, this.canvasCTX);
        }
        if ("text_blocks" in inputObject) {
            for (let textBlock of inputObject.text_blocks) {
                new CanvasTextDrawer(textBlock, this.canvasCTX)
            }
        }
    }
}