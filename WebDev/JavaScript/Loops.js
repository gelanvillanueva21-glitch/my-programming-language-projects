
var x = 0

while (x <= 5) {
    console.log(x)
    x += 1
}

x = 0

do {
    console.log(x)
    x += 1
} while (x <= 5);
console.log("")
var y = [1, 3, 5, 7]
for (const [i, element] of y.entries()) {
    console.log(i, element)
} console.log("")

for (let index = 0; index < y.length; index++) {
    console.log(y[index])
}