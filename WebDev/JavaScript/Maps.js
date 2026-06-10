var myMap = new Map();
var numMap = new Map([[1, "one"], [2, "two"]]);

myMap.set("firstname", "Gelan")
myMap.set("secondname", "Mar")
myMap.set("middlename", "Go")
myMap.set("lastname", "Villanueva")


console.log(myMap.has("firstname"));
console.log(myMap.size);

for (const [key, val] of myMap) {
    console.log(key, val);
}
