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
 

const CANVAS_DATA = {"all_objects": [{"all_coordinates": null, "all_objects": [{"all_coordinates": [[798.5714285714286, 598.5714285714286], [683.8095238095239, 598.5714285714286], [683.8095238095239, 489.04761904761904], [798.5714285714286, 489.04761904761904], [798.5714285714286, 598.5714285714286]], "all_objects": [], "strokeColor": "green", "lineWidth": 2, "text_blocks": [{"text": "1150.0", "all_coordinates": [741.1904761904761, 543.8095238095239]}]}, {"all_coordinates": [[689.047619047619, 598.5714285714286], [574.2857142857143, 598.5714285714286], [574.2857142857143, 379.5238095238095], [689.047619047619, 379.5238095238095], [689.047619047619, 598.5714285714286]], "all_objects": [], "strokeColor": "green", "lineWidth": 2, "text_blocks": [{"text": "2300.0", "all_coordinates": [631.6666666666666, 489.04761904761904]}]}, {"all_coordinates": [[579.5238095238095, 598.5714285714286], [464.76190476190476, 598.5714285714286], [464.76190476190476, 360.4761904761905], [579.5238095238095, 360.4761904761905], [579.5238095238095, 598.5714285714286]], "all_objects": [], "strokeColor": "green", "lineWidth": 2, "text_blocks": [{"text": "2500.0", "all_coordinates": [522.1428571428571, 479.5238095238095]}]}, {"all_coordinates": [[470.0, 598.5714285714286], [355.23809523809524, 598.5714285714286], [355.23809523809524, 360.4761904761905], [470.0, 360.4761904761905], [470.0, 598.5714285714286]], "all_objects": [], "strokeColor": "green", "lineWidth": 2, "text_blocks": [{"text": "2500", "all_coordinates": [412.6190476190476, 479.5238095238095]}]}, {"all_coordinates": [[360.4761904761905, 598.5714285714286], [245.71428571428572, 598.5714285714286], [245.71428571428572, 360.4761904761905], [360.4761904761905, 360.4761904761905], [360.4761904761905, 598.5714285714286]], "all_objects": [], "strokeColor": "green", "lineWidth": 2, "text_blocks": [{"text": "2500.0", "all_coordinates": [303.0952380952381, 479.5238095238095]}]}, {"all_coordinates": [[250.95238095238096, 598.5714285714286], [136.1904761904762, 598.5714285714286], [136.1904761904762, 384.2857142857143], [250.95238095238096, 384.2857142857143], [250.95238095238096, 598.5714285714286]], "all_objects": [], "strokeColor": "green", "lineWidth": 2, "text_blocks": [{"text": "2250.0", "all_coordinates": [193.57142857142858, 491.42857142857144]}]}, {"all_coordinates": [[141.42857142857142, 598.5714285714286], [26.666666666666668, 598.5714285714286], [26.666666666666668, 493.8095238095238], [141.42857142857142, 493.8095238095238], [141.42857142857142, 598.5714285714286]], "all_objects": [], "strokeColor": "green", "lineWidth": 2, "text_blocks": [{"text": "1100.0", "all_coordinates": [84.04761904761905, 546.1904761904761]}]}], "strokeColor": null, "lineWidth": null, "text_blocks": []}]}
const CANVAS_SLOPE = {"all_objects": [{"all_coordinates": [[798.5714285714286, 598.5714285714286], [36.666666666666664, 598.5714285714286], [274.76190476190476, 360.4761904761905], [560.4761904761905, 360.4761904761905], [798.5714285714286, 598.5714285714286]], "all_objects": [], "strokeColor": "rgba(255, 0, 0, 0.5)", "lineWidth": 2, "text_blocks": []}]}


let compos = new CanvasCompositionDrawer([CANVAS_DATA], ctx)
let slope = new CanvasCompositionDrawer([CANVAS_SLOPE], ctx)
