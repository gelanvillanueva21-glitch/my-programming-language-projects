// var arr = [1, 2, "Hello World", true]
// console.log(arr[arr.length - 2])

// var arr2 = [1, 4, "gyat", true]
// var arr3 = arr.concat(arr2)
// console.log(arr3)

// var arr4 = arr3.splice(1, 6)
// console.log(arr4)
// console.log(arr3)

const [x, x2, ...y] = [1, 2, 3, 4, 5]
console.log(x, x2, y)


var k = [1, 2, 3, 4, 5]
var i = [...k]
i.push("Hello")
console.log(k, i)