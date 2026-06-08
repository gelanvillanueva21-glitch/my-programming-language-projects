const numbers = [1, 2, 3, 4];
const doubled = numbers.map((num) => num * 2);
console.log(doubled);

const users = [
    { name : "Alice", age : 25},
    { name : "Cookie", age : 30}
]

const names = users.map((user) => user.name);
console.log(names);

const numbers2 = [1 ,2 ,3 ,4 , 5]
const sum = numbers2.reduce((acc, num) => acc + num, 0)
console.log(sum);

const numbers3 = [2, 3, 6, 7, 10]
const result = numbers3.filter((num) => num % 2 === 0)
console.log(result);
