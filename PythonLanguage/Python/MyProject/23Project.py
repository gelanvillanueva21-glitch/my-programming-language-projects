import random

class Dice():
	def roll(self):
		num_dots = (1, 2, 3, 4, 5, 6)
		roll1 = random.choice(num_dots)
		roll2 = random.choice(num_dots)
		print(f"({roll1}, {roll2})")
		
		
dice = Dice()
dice.roll()