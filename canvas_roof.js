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
        this.setContectDefault()
    }
    setContectDefault() {
        if (this.strokeWidth) {
            this.canvasCTX.strokeStyle = "#000000";
        }
        if (this.strokeColor) {
            this.canvasCTX.lineWidth = 1;
        }
    }
}

class CanvasObjectDrawer {
    constructor(object, canvasCTX) {
        new CanvasDrawer(object.strokeColor, object.strokeWidth, canvasCTX, object.coordinates)
    }
}


class CanvasCompositionDrawer {
    constructor(allObjectsToDraw, canvasCTX) {
        for (let object of allObjectsToDraw) {
            new CanvasObjectDrawer(object, canvasCTX)
        }
    }
}