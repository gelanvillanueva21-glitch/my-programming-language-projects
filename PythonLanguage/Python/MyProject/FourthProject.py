num = int(input("Guess: "))
number = 1
while num > 9 or num < 9:
	number = number + 1
	num = int(input("Guess: "))
	
	if number == 3:
		print('Limit Of Guesses')
		break

if num == 9:
	print("Correct")
		
print("Done")