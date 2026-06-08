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
                temporaryList.push(element[2])
        }
        return temporaryList
    }
    helperNameList() {
        return this.studentInfo
            .filter((student) => student[2] >= 70)
            .map((student) => student[0])
    }
    getLetterGrade(name) {

        for (const element of this.studentInfo) {
            if (name === element[0]) 
                var gradeNumber = element[2]
        }

        if (gradeNumber >= 90)
            return "A"
        else if (gradeNumber >= 80)
            return "B"
        else if (gradeNumber >= 70)
            return "C"
        else
            return "F"
    }
}

console.log("Welcome to the Script University\nPlease enter how many students you want\nEnter Correct answer to the Specific question");

try {
    var numberOfStudent = Number(prompt("> "))
    var studentInfo = []

    while (numberOfStudent > 0) {
        const tmpStudentInfo = []
        let studetName = prompt("Enter Student Full Name: ")
        tmpStudentInfo.push(studetName)

        let studentAge = Number(prompt("Enter Student Age: "))
        tmpStudentInfo.push(studentAge)

        let studentGrade = Number(prompt("Enter Student Grade: "))
        tmpStudentInfo.push(studentGrade)

        studentInfo.push(tmpStudentInfo)
        numberOfStudent -= 1
    }
    while (true) {
        const schoolUni = new ScriptUniversity(studentInfo)
        console.log(`\nThere are aproximatly ${studentInfo.length} student you entered\n`);
        console.log("-----MENU's-----\n1. Get highest grade from the student list\n2. Get Student Info\n3. Get Letter Grade\n4. Exit Program");
        const choice = Number(prompt("> "))

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
} catch (error) {
    console.log(error.message);
}

