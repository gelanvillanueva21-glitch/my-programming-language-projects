const prompt = require("prompt-sync")()

class ScriptUniversity {
    constructor(studentInfo) {
        this.studentInfo = studentInfo
    }
    getHighest() {
        const gradeList = this.helperGradeList()
        var tmpVar = gradeList[0]
        for (let i = 0; i < gradeList.length; i++) {
            if (gradeList[i] >= tmpVar)
                tmpVar = gradeList[i]
        }
        console.log(gradeList);
        return tmpVar
    }
    getStudentInfo() {
        console.log("\n-----Students Info-----");
        for (const infos of this.studentInfo) {
            console.log(`Name:  ${infos[0]}`);
            console.log(`Age:  ${infos[1]}`);
            console.log(`Grade:  ${infos[2]}`);
        }
    }
    helperGradeList() {
        const temporaryList = [] 
        for (const element of this.studentInfo) {
            if (element[2] > 50) 
                temporaryList.push(element)
        }
        console.log(temporaryList);
        return temporaryList
    }
    helperNameList() {
        const gradeList = this.helperGradeList()
        const resultGradeList = gradeList.map((number) => number < 70)
        const tmpNameList = []
        for (const i of resultGradeList) {
            for (const y of this.studentInfo) {
                if (y == i)
                    tmpNameList.push(y)
            }
        }
        console.log(gradeList);
        return tmpNameList
    }
    getLetterGrade(name) {
        let grade = new Map()
        grade.set(90, "A")
        grade.set(80, "B")
        grade.set(70, "C")

        for (const element of this.studentInfo) {
            if (name === element[0]) 
                var gradeNumber = element[2]
        }

        for (const [key, val] of grade) {
            if (gradeNumber >= key)
                return val
            else
                return "F"
        }
    }
}

console.log("Welcome to the Script University\nPlease enter how many students you want\nEnter Correct answer to the Specific question");
var numberOfStudent = prompt("> ")
var studentInfo = []

while (numberOfStudent > 0) {
    const tmpStudentInfo = []
    let studetName = prompt("Enter Student Full Name: ")
    tmpStudentInfo.push(studetName)

    let studentAge = prompt("Enter Student Age: ")
    tmpStudentInfo.push(studentAge)

    let studentGrade = number(prompt("Enter Student Grade: "))
    tmpStudentInfo.push(studentGrade)

    studentInfo.push(tmpStudentInfo)
    numberOfStudent -= 1
}
while (true) {
    const schoolUni = new ScriptUniversity(studentInfo)
    console.log(`\nThere are aproximatly ${studentInfo.length} student you entered\n`);
    console.log("-----MENU's-----\n1. Get highest grade from the student list\n2. Get Student Info\n3. Get Letter Grade\n4. Exit Program");
    const choice = prompt("> ")

    if (choice == 1) {
        console.log(schoolUni.getHighest());
    } else if (choice == 2) {
        schoolUni.getStudentInfo();
    } else if (choice == 3) {
        const name = prompt("Enter Name: ")
        console.log(`Grade:  ${schoolUni.getLetterGrade(name)}`);
    } else if (choice == 4) {
        console.log("-----Students Passed-----");
        console.log(schoolUni.helperNameList());
        break
    }
}