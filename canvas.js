var canvas = document.getElementById("example"),
    ctx = example.getContext('2d');
ctx.transform(1, 0, 0, -1, 0, canvas.height)


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

let compos = new CanvasCompositionDrawer(allObjects, ctx)