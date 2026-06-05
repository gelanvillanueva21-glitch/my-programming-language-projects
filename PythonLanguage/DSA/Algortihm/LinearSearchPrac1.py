def search_student(students, name):
    #Searching in a linear loop each iteration
    for index in range(len(students)):
        if students[index] == name:
            return index
    else:
        return "Name not found"

students = ["Gelan", "Arnie", "Molly ", "Cookie", "Chanzine"]

print(f"> {search_student(students, "Zoro")}")
print(f"> {search_student(students, "Chanzine")}")
print(f"> {search_student(students, "Gelan")}")


