var object = {
    name: "Gelan",
    birthdate: [9, 9, 2007],
    newObj: {
        laptop: "HP"
    }
}

console.log(object);
console.log(Object.values(object));

var object2 = {
    sung: "Jinwu",
    num: [1, 2, 3, 4, 5]
}

for (const key in object) {
    console.log(key);
}

var object3 = {...object, ...object2}
console.log(object3);
console.log(object.newObj.laptop);
