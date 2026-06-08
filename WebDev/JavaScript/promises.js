const myPromise = new Promise((resolve, reject) => {
    if (true) {
        resolve("Good");
    } else {
        reject("Bad");
    }
})

myPromise.then((value) => {
    console.log(value)
}).catch((value) => {
    console.log(value);
})