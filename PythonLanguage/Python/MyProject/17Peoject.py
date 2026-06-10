Secret_Number = 94

try:
	print("Guess The Number")
	
	while True:
		guess = int(input("> "))
		
		if guess == Secret_Number:
			print("Correct!")
			break
		else:
			print("Wrong")
			
except ValueError:
	print("Invalid Input!")