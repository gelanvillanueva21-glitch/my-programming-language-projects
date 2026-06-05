class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, other_character):
        print("Character attacks!")
        
class Warrior(Character):
    def attack(self, other_character):
        damage = 20
        other_character.health -= damage
        print(f"{self.name} attacks {other_character.name} for {damage} damage!")
        print(f"{other_character.name} health: {other_character.health}")
        
class Mage(Character):
    def attack(self, other_character):
        damage = 15
        other_character.health -= damage
        print(f"{self.name} attacks {other_character.name} for {damage} damage!")
        print(f"{other_character.name} health: {other_character.health}")
        
warrior = Warrior("Thor", 100)
mage = Mage("Merlin", 80)

warrior.attack(mage)
mage.attack(warrior)