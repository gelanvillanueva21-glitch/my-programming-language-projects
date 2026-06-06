const prompt = require("prompt-sync")()
var FirstName = prompt("Enter Your First Name: ")
var MiddleName = prompt("Enter Your Middle Name: ")
var LastName = prompt("Enter Your Last Name: ")
console.log("Full Name: ",FirstName, MiddleName, LastName)

console.log("1. Change First Name\n2. Change Middle Name\n3. Change Last Name")
var Choice = prompt("> ")
if (Choice == 1) {
    FirstName = prompt("Enter New First Name: ")
} else if (Choice == 2) {
    MiddleName = prompt("Enter New Middle Name: ")
} else if (Choice == 3) {
    LastName = prompt("Enter New Last Name: ")
}
console.log(FirstName, MiddleName, LastName)