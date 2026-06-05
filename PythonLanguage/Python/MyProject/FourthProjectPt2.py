secret_num = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
	guess = int(input("Guess: "))
	guess_count += 1
	
	if guess == secret_num:
		print("You Won!")
		break
	elif guess_count == guess_limit:
		print("You Lose!")
		