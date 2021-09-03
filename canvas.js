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
 

const CANVAS_DATA = {"all_objects": [{"all_coordinates": null, "all_objects": [{"all_coordinates": [[1.4285714285714286, 598.5714285714286], [116.19047619047619, 598.5714285714286], [116.19047619047619, 379.5238095238095], [1.4285714285714286, 379.5238095238095], [1.4285714285714286, 598.5714285714286]], "all_objects": [], "strokeColor": "green", "lineWidth": 2, "text_blocks": [{"text": "2300", "all_coordinates": [58.80952380952381, 489.04761904761904]}]}, {"all_coordinates": [[110.95238095238095, 598.5714285714286], [225.71428571428572, 598.5714285714286], [225.71428571428572, 160.47619047619048], [110.95238095238095, 160.47619047619048], [110.95238095238095, 598.5714285714286]], "all_objects": [], "strokeColor": "green", "lineWidth": 2, "text_blocks": [{"text": "4600", "all_coordinates": [168.33333333333334, 379.5238095238095]}]}, {"all_coordinates": [[220.47619047619048, 598.5714285714286], [335.23809523809524, 598.5714285714286], [335.23809523809524, 27.142857142857142], [220.47619047619048, 27.142857142857142], [220.47619047619048, 598.5714285714286]], "all_objects": [], "strokeColor": "green", "lineWidth": 2, "text_blocks": [{"text": "6000", "all_coordinates": [277.85714285714283, 312.85714285714283]}]}, {"all_coordinates": [[330.0, 598.5714285714286], [444.76190476190476, 598.5714285714286], [444.76190476190476, 112.85714285714286], [330.0, 112.85714285714286], [330.0, 598.5714285714286]], "all_objects": [], "strokeColor": "green", "lineWidth": 2, "text_blocks": [{"text": "5100", "all_coordinates": [387.3809523809524, 355.7142857142857]}]}, {"all_coordinates": [[439.5238095238095, 598.5714285714286], [554.2857142857143, 598.5714285714286], [554.2857142857143, 331.9047619047619], [439.5238095238095, 331.9047619047619], [439.5238095238095, 598.5714285714286]], "all_objects": [], "strokeColor": "green", "lineWidth": 2, "text_blocks": [{"text": "2800", "all_coordinates": [496.9047619047619, 465.23809523809524]}]}, {"all_coordinates": [[549.047619047619, 598.5714285714286], [663.8095238095239, 598.5714285714286], [663.8095238095239, 550.952380952381], [549.047619047619, 550.952380952381], [549.047619047619, 598.5714285714286]], "all_objects": [], "strokeColor": "green", "lineWidth": 2, "text_blocks": [{"text": "500", "all_coordinates": [606.4285714285714, 574.7619047619048]}]}], "strokeColor": null, "lineWidth": null, "text_blocks": []}]}
const CANVAS_SLOPE ={"all_objects": [{"all_coordinates": [[1.4285714285714286, 598.5714285714286], [572.8571428571429, 598.5714285714286], [287.14285714285717, 27.142857142857142], [1.4285714285714286, 598.5714285714286]], "all_objects": [], "strokeColor": "rgba(255, 0, 0, 0.5)", "lineWidth": 2, "text_blocks": []}]}


let compos = new CanvasCompositionDrawer([CANVAS_DATA], ctx)
let slope = new CanvasCompositionDrawer([CANVAS_SLOPE], ctx)
