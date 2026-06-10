class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, other):
        other.health -= self.damage
        print(f"{self.name} attacked {other.name} for {self.damage} damage!")

    def show_stats(self):
        print(f"\nName: {self.name} | Health: {self.health} | Damage: {self.damage}\n")


class Player(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.inventory = []

    def attack(self, other):
        if "gun" in self.inventory:
            other.health -= 300
            print("You used the gun! Massive damage!")
        else:
            super().attack(other)


class Enemy(Character):
    pass


def main():
    player = Player("Gelan", 100, 50)
    enemy = Enemy("Iron Golem", 500, 30)

    while True:
        print("\n1. Look Around\n2. Attack\n3. Player Stats\n4. Enemy Stats\n5. Quit")
        try:
            choice = int(input("> "))
        except ValueError:
            print("Enter a number!")
            continue

        if choice == 1:
            print("You found a gun!")
            player.inventory.append("gun")
        elif choice == 2:
            player.attack(enemy)
            if enemy.health <= 0:
                print("Enemy defeated!")
                break
            enemy.attack(player)
            if player.health <= 0:
                print("You died!")
                break
        elif choice == 3:
            player.show_stats()
        elif choice == 4:
            enemy.show_stats()
        elif choice == 5:
            break
        else:
            print("Invalid input")

main()