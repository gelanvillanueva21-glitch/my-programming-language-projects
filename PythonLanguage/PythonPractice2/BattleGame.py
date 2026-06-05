import random as ran

class Game:
    def __init__(self, 
        char_name, char_damage, char_health, 
        enemy_name, enemy_damage, enemy_health):

        self.char_name = char_name
        self.char_damage = char_damage
        self.char_health = char_health
        self.enemy_name = enemy_name
        self.enemy_damage = enemy_damage
        self.enemy_health = enemy_health


    def attack(self):
        num = ran.randint(1, 3)
        self.enemy_health -= self.char_damage

        print(f"{self.char_name} attacked {self.enemy_name}")
        if num == 2:
            self.char_health -= self.enemy_damage
            print(f"{self.enemy_name} attacked {self.char_name}")
        else:
            print("You Dodged An Attack")

    def character_Info(self):
        print(f""" 
Character Name: {self.char_name}
Damage: {self.char_damage}
Health: {self.char_health}""")

    def enemy_Info(self):
        print(f"""
Enemy Name: {self.enemy_name}
Damage: {self.enemy_damage}
Health: {self.enemy_health}""")



    def main(self):
        while True:
            try:
                print("\n1. Attack\n2. Character Info\n3. Enemy Info\n4. Exit")
                choice = int(input("> "))

                if choice == 1:
                    self.attack()
                elif choice == 2:
                    self.character_Info()
                elif choice == 3:
                    self.enemy_Info()
                elif choice == 4:
                    break
                else:
                    print("Input Not Found")
            except ValueError:
                print("Enter A Number!")
                continue

game = Game('Gelan', 500, 1000, 'Kratos', 250, 10000)
game.main()