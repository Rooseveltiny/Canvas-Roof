var canvas = document.getElementById("example"),
    ctx = example.getContext('2d');

// ctx.transform(1, 0, 0, -1, 0, canvas.height)

obj0 = {
    coordinates: [[1.5, 1.5], [1201.5, 1.5], [651.5, 601.5], [551.5, 601.5], [1.5, 1.5]],
    strokeColor: "blue",
    strokeWidth: 3
}

obj1 = {
    coordinates: [[1.5, 1.5], [122, 1.5], [122, 126.9], [1.5, 126.9], [1.5, 1.5]],
    strokeColor: "rgba(0, 0, 200, 0.5)",
    strokeWidth: 3
}


obj2 = {
    coordinates: [[116.5, 1.5], [237, 1.5], [237, 252.4], [116.5, 252.4], [116.5, 1.5]],
    strokeColor: "rgba(0, 0, 200, 0.5)",
    strokeWidth: 3
}

obj3 = {
    coordinates: [[231.5, 1.5], [352, 1.5], [352, 377.3], [231.5, 377.8], [231.5, 1.5]],
    strokeColor: "rgba(0, 0, 200, 0.5)",
    strokeWidth: 3
}

obj4 = {
    coordinates: [[346.5, 1.5], [467, 1.5], [467, 503.3], [346.5, 503.3], [346.5, 1.5]],
    strokeColor: "rgba(0, 0, 200, 0.5)",
    strokeWidth: 3
}

obj5 = {
    coordinates: [[461.5, 1.5], [582, 1.5], [582, 601.5], [461.5, 601.5], [461.5, 1.5]],
    strokeColor: "rgba(0, 0, 200, 0.5)",
    strokeWidth: 3
}

obj6 = {
    coordinates: [[576.5, 1.5], [697, 1.5], [697, 601.5], [576.5, 601.5], [576.5, 1.5]],
    strokeColor: "rgba(0, 0, 200, 0.5)",
    strokeWidth: 3
}

obj7 = {
    coordinates: [[691.5, 1.5], [812, 1.5], [812, 557.8], [691.5, 557.8], [691.5, 1.5]],
    strokeColor: "rgba(0, 0, 200, 0.5)",
    strokeWidth: 3
}
obj8 = {
    coordinates: [[806.5, 1.5], [927, 1.5], [927, 432.4], [806.5, 432.4], [806.5, 1.5]],
    strokeColor: "rgba(0, 0, 200, 0.5)",
    strokeWidth: 3
}
obj9 = {
    coordinates: [[921.5, 1.5], [1042, 1.5], [1042, 306.9], [921.5, 306.9], [921.5, 1.5]],
    strokeColor: "rgba(0, 0, 200, 0.5)",
    strokeWidth: 3
}

obj10 = {
    coordinates: [[1036, 1.5], [1157, 1.5], [1157, 181.5], [1036, 181.5], [1036, 1.5]],
    strokeColor: "rgba(0, 0, 200, 0.5)",
    strokeWidth: 3
}

obj11 = {
    coordinates: [[1151, 1.5], [1272, 1.5], [1272, 56.0], [1151, 56.0], [1151, 1.5]],
    strokeColor: "rgba(0, 0, 200, 0.5)",
    strokeWidth: 3
}

allObjects = [
    obj0,
    obj1,
    obj2,
    obj3,
    obj4,
    obj5,
    obj6,
    obj7,
    obj8,
    obj9,
    obj10,
    obj11,
]

// let compos = new CanvasCompositionDrawer([CANVAS_DATA], ctx)
 

const CANVAS_DATA = {"all_objects": [{"all_coordinates": null, "all_objects": [{"all_coordinates": [[1497.142857142857, 597.1428571428571], [1268.5714285714287, 597.1428571428571], [1268.5714285714287, 25.714285714285715], [1497.142857142857, 25.714285714285715], [1497.142857142857, 597.1428571428571]], "all_objects": [], "strokeColor": "green", "lineWidth": 2, "text_blocks": [{"text": "3000", "all_coordinates": [1382.857142857143, 311.42857142857144]}]}, {"all_coordinates": [[1278.095238095238, 597.1428571428571], [1049.5238095238096, 597.1428571428571], [1049.5238095238096, 25.714285714285715], [1278.095238095238, 25.714285714285715], [1278.095238095238, 597.1428571428571]], "all_objects": [], "strokeColor": "green", "lineWidth": 2, "text_blocks": [{"text": "3000", "all_coordinates": [1163.8095238095239, 311.42857142857144]}]}, {"all_coordinates": [[1059.047619047619, 597.1428571428571], [830.4761904761905, 597.1428571428571], [830.4761904761905, 25.714285714285715], [1059.047619047619, 25.714285714285715], [1059.047619047619, 597.1428571428571]], "all_objects": [], "strokeColor": "green", "lineWidth": 2, "text_blocks": [{"text": "3000", "all_coordinates": [944.7619047619048, 311.42857142857144]}]}, {"all_coordinates": [[840.0, 597.1428571428571], [611.4285714285714, 597.1428571428571], [611.4285714285714, 25.714285714285715], [840.0, 25.714285714285715], [840.0, 597.1428571428571]], "all_objects": [], "strokeColor": "green", "lineWidth": 2, "text_blocks": [{"text": "3000", "all_coordinates": [725.7142857142857, 311.42857142857144]}]}, {"all_coordinates": [[620.952380952381, 597.1428571428571], [392.3809523809524, 597.1428571428571], [392.3809523809524, 25.714285714285715], [620.952380952381, 25.714285714285715], [620.952380952381, 597.1428571428571]], "all_objects": [], "strokeColor": "green", "lineWidth": 2, "text_blocks": [{"text": "3000", "all_coordinates": [506.6666666666667, 311.42857142857144]}]}, {"all_coordinates": [[401.9047619047619, 597.1428571428571], [173.33333333333334, 597.1428571428571], [173.33333333333334, 25.714285714285715], [401.9047619047619, 25.714285714285715], [401.9047619047619, 597.1428571428571]], "all_objects": [], "strokeColor": "green", "lineWidth": 2, "text_blocks": [{"text": "3000", "all_coordinates": [287.6190476190476, 311.42857142857144]}]}], "strokeColor": null, "lineWidth": null, "text_blocks": []}]}
const CANVAS_SLOPE = {"all_objects": [{"all_coordinates": [[1497.142857142857, 597.1428571428571], [354.2857142857143, 597.1428571428571], [354.2857142857143, 25.714285714285715], [1497.142857142857, 25.714285714285715], [1497.142857142857, 597.1428571428571]], "all_objects": [], "strokeColor": "rgba(255, 0, 0, 0.5)", "lineWidth": 2, "text_blocks": []}]}


let compos = new CanvasCompositionDrawer([CANVAS_DATA], ctx)
let slope = new CanvasCompositionDrawer([CANVAS_SLOPE], ctx)
