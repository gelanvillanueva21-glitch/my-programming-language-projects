quizes = int(input("Enter Quize (1-20) Score: "))
performance_task = int(input("Enter PT (1-100) Score: "))
exam = int(input("Enter Exam (1-50) Score: "))

Quiz = (quizes / 20) * 100
PT = (performance_task / 100) * 100
Exam = (exam / 50) * 100
Final_Grades = (Quiz * 0.20) + (PT * 0.30) + (Exam * 0.50)

print("Your Grades Is " ,Final_Grades)

if Final_Grades > 100:
	print("You Cant Get above 100 Grades")
elif Final_Grades >= 95:
	print("You Got A Highest Honor")
	print("Pass")
elif Final_Grades >= 90:
	print("You Got High Honor")
	print("Pass")
elif Final_Grades >= 85:
	print("You Got Honor")
	print("Pass")
elif Final_Grades >= 80:
	print("Nice Grades")
	print("Pass")
elif Final_Grades >= 65:
	print("Pass")
else:
	print("Failed")
