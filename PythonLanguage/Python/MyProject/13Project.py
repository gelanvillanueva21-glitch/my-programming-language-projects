print("""
This is the number guessing game.
You have only three guesses to win.
Goodluck my boy!!!

    """)

Secret_Number = 90
Num_Of_Guesses = 3

while Num_Of_Guesses > 0:
	
	Guess_Number = int(input("> "))
	
	if Guess_Number > Secret_Number:
		print("You Guess it High!")
	elif Guess_Number < Secret_Number:
		print("You Guess it Low!")
	elif Guess_Number == Secret_Number:
		print("Correct!")
		print("Your Number Of Guess: " , Num_Of_Guesses )
		break
	
	print("")
	Num_Of_Guesses -= 1
	
else:
	print("You Fail!")