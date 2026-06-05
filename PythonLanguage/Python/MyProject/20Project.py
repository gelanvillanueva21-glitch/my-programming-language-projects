class Character:
	def __init__(self, name, health):
		self.name = name
		self.health = health
		
	def attack(self):
		print("Character Attacked!")
		
class Warrior(Character):
	def attack(self):
		print(f"{self.name} Health {self.health}")
		
		
class Mage(Character):
	def attack(self):
		print(f"{self.name} Health {self.health} ")
		

warrior = Warrior("Thor", 20)
mage = Mage("Ash", 15)

warrior.attack()
mage.attack()