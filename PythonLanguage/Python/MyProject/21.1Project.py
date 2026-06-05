import random

class Character:
	def __init__(self, name, health, damage):
		self.name = name
		self.health = health
		self.damage = damage
	
	def dictionary(self):
		
		print(f"Name: {self.name} | Health: {self.health} | Damage: {self.damage}")
		
	def character_stats(self):
		print(f"\nName: {self.name}\nHealth: {self.health}")
		
		
	def attack(self, other):
		other.health -= self.damage
		print(f"{self.name} Attack {other.name} for {self.damage}")
		
	
class Player(Character):
	def __init__ (self, name, health, damage):
		super().__init__(name, health, damage)
		self.inventory = []
		
		
	def attack(self, other):
		if "Gun" and "Potion" and "Katana" in self.inventory:
			print("---Tools---")
			num = 1
			for i in self.inventory:
				print(f"{num}. {i}")
				num += 1
			tool_to_use = input("> ")
			while True:
				if tool_to_use == "Gun":
					other.health -= 750
					print("You Use A Gun!!")
					print("Massive Damage!")
					break
				elif tool_to_use == "Potion":
					self.health += 1500
					print("You Drink A Potion")
					print("Massive Health!!")
					break
				elif tool_to_use == "Katana":
					other.health -= 1000
					print("You Deal Massive Damage To Enemy!")
					break
				else:
					print("No Tools")
		else:
				super().attack(other)
			
	
	
class Enemy(Character):
	def attack(self, other):
		super().attack(other)
		
		
	def enemy_spawn(self):
		print(f"\nA {self.name} Enemy Spawn\n With A {self.health} Health")
	

class Gameplay:	
	def main(self):
		while True:
			user = input("Create Player Name: ")
			if len(user) >= 5:
				break
			else:
				print("Must Atleast 5 Letters")
		
		while True:
			player = Player(user, 500, 250)
			easy_enemy = Enemy("Ogre", 1000, 95)
			normal_enemy = Enemy("Giant Golem", 5000, 100)
			hard_enemy = Enemy("Dragon", 10000, 120)
			print("\n1. Play Game\n2. Characters Dictionary\n3. Quit")
			try:
				choice = int(input("> "))
			except ValueError:
				print("Input Number!!!")
				continue
				
			if choice == 1:
				def game():
					while True:
						print("\n1. Easy\n2. Normal\n3. Hard")
						try:
							choose = int(input("> "))
						except ValueError:
							print("Input Number!")
						if choose == 1:
							print("Easy Mode")
							easy_enemy.enemy_spawn()
							break
						elif choose == 2:
							print("Normal Mode")
							normal_enemy.enemy_spawn()
							break
						elif choose == 3:
							print("Hard Mode")
							hard_enemy.enemy_spawn()
							break
						else:
								print("Wrong Input!")
					while True:
						num = random.randint(1,4)
						if player.health <= 0:
							print("Player Died!")
							return
						print("\n1. Attack\n2. Run\n3. Player Stat\n4. Enemy Stat")
						try:
							choice = int(input("> "))
						except ValueError:
							print("Input Number!!!")
							continue
							
						if choice == 1:
							if choose == 1:
								if easy_enemy.health <= 10:
									print(f"You Defeated The {easy_enemy.name}!!")
									return
								player.attack(easy_enemy)
								if num == 2:
									easy_enemy.attack(player)
							elif choose == 2:
								if normal_enemy.health <= 10:
									print(f"You Defeated The {normal_enemy.name}!!")
									return
								player.attack(normal_enemy)
								if num == 2:
									normal_enemy.attack(player)
							elif choose == 3:
								if hard_enemy.health <= 10:
									print(f"You Defeated The {hard_enemy.name}")
									return
								player.attack(hard_enemy)
								if num == 3:
									hard_enemy.attack(player)
						elif choice == 2:
							print("\n1. Bathroom\n2. Cabinet\n3. Backyard\n4. Kitchen\n5. Dojo")
							while True:
								try:
									choice_run = int(input("> "))
								except ValueError:
									print("Input Number!!!")
								
								if choice_run == 1:
									print("Nothing Here")
									break
								elif choice_run == 2:
									print("You Found A Gun!")
									player.inventory.append("Gun")
									break
								elif choice_run == 3:
									print("You Step On The Poop")
									break
								elif choice_run == 4:
									print("You Are In The Bathroom\nYou Found A Potion")
									player.inventory.append("Potion")
									break
								elif choice_run == 5:
									print("You Are In The Dojo\nYou Found A Katana!")
									player.inventory.append("Katana")
									break
								else:
									print("Nothing Here")
						elif choice == 3:
							player.character_stats()
						elif choice == 4:
							if choose == 1:
								easy_enemy.character_stats()
							elif choose == 2:
								normal_enemy.character_stats()
							elif choose == 3:
								hard_enemy.character_stats()
						else:
							print("Wrong Input!")
							
				game()
			elif choice == 2:
				player.dictionary()
				easy_enemy.dictionary()
				normal_enemy.dictionary()
				hard_enemy.dictionary()
			elif choice == 3:
				return
			else:
				print("Wrong Input")
		
		
game = Gameplay()
game.main()