print("1. Work")
print("2. Rest")
print("3. Workout")
print("4. Eat")
print("5. Stop")
energy = 10
days = 0
kilo_gram = 50.0
muscle_mass = 23.0
loop_stop_continue = True

while loop_stop_continue:
	print(f'Day {days}')
	print(f'Your Weight Is {kilo_gram}')
	print(f'Your Musclemass is {muscle_mass}')
	print(f'Your Energy is {energy}')
	pick = str(input("Enter: ")).capitalize()
	
	if energy <= 0:
		print("You are exhausted")
		loop_stop_continue = False
	elif energy < 3:
		print("You are too exhausted")
	elif energy < 5:
		print(" You are tired")
	elif energy < 8:
		print("You are body needs rest")
	else:
		print("You have enough energy")
	
	if pick == '1' or pick == 'Work':
		energy -= 1
		print("You Finished Working")
		print("You Lost 1 Energy")
		print("Rest To Gain Energy")
	elif pick == '2' or pick == 'Rest':
		energy += 1
		print("You Sleep Well")
		print("You Rest Well")
		print("You Gain 1 Energy")
	elif pick == '3' or pick == 'Workout':
		energy -= 1
		muscle_mass += 0.2
		kilo_gram -= 0.2
		print("You Finished Workout")
		print(f"Your Current Muscle  {muscle_mass} kg")
		print("Rest To Recover And Eat Plenty")
	elif pick == '4' or pick == 'Eat':
		print("You've Finished Eat")
		kilo_gram += 0.45
	elif pick == '5' or pick == 'Stop':
		loop_stop_continue = False
	else:
		print("incorrect Input")
	days += 1
	
print("Program Done")