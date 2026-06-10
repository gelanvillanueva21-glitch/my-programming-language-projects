class Character:
	def __init__(self, name, health, damage):
		self.name = name
		self.health = health
		self.damage = damage
		
	def attack(self, other):
		other.health -= self.damage
		print(f"{self.name} Attacked {other.name} for {self.damage} damage")
		
		
	def show_stats(self):
		print(f"\nName: {self.name} | Health: {self.health} | Damage: {self.damage}")
		
class Player(Character):
	def __init__(self, name, health, damage):
		super().__init__(name, health, damage)
		self.inventory = []
		
	def attack(self, other):
		if "gun" in self.inventory:
			other.health -= 350
			print("You used gun! deals massive damage!")
		else:
			super().attack(other)
	
class Enemy(Character):
	pass
	
	
def Main():
	player = Player("Gelan", 400, 50)
	enemy = Enemy("Warden", 700, 75)
	print("\n1. Look Around\n2. Attack\n3. Player Stats\n4. Enemy Stats\n5. Quit")
	while True:
		try:
			choice = int(input("> "))
		except ValueError:
			print("Enter A Number!")
			continue
			
		if choice == 1:
			print("\nYou Found A Gun!")
			player.inventory.append("gun")
		elif choice == 2:
			player.attack(enemy)
			if enemy.health <= 0:
				print("Enemy Defeated")
				break
			if player.health <= 0:
				print("You Died")
				break
		elif choice == 3:
			player.show_stats()
		elif choice == 4:
			enemy.show_stats()
		elif choice == 5:
			return
		else:
			print("Incorrect Input")
	
Main()