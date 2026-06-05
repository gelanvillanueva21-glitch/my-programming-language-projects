
class Inventory:
    def __init__(self):
        self.inventory = {
            "Potion" : [],
            "Armor" : [],
            "Tools" : [],
            "Others" : []
        }
        self.equipedItem = {
            "Armor" : {
                "Helmet" : None,
                "Chestplate" : None,
                "Leggings" : None,
                "Boots" : None
            },
            "Tool" : ["Excalibur", 500, ["World Slash", 9999], 100]
        }


    def addItem(self, items):
        if self.isMaxInv():
            print("\nInventory Maximum Capacity\n")
            return
        for value, item in self.inventory.items():
            if value in items:
                self.inventory[value].append(items[1])


    def removeItem(self, items):
        for value, item in self.inventory.items():
            if value in items:
                self.inventory[value].remove(items[1])
                return f"\n{items[1]} successfully Removed\n"
        return f"\n{items[1]} not Found\n"


    def usePotion(self, potion):
        if self.inventory["Potion"] == []:
            print("\nPotion Is Empty, Can't Use Potion\n")
            return
        for item in self.inventory["Potion"]:
            if item == potion:
                self.inventory["Potion"].remove(potion)
                print(f"\n{potion} successfully Used\n")
                for i, y in {
                    "Health Potion" : 50, 
                    "Mana Potion" : 100, 
                    "Damage Potion" : 150, 
                    "Crit Potion" : 1.8}.items():
                    if potion == i:
                        return y
        return f"\n{potion} not Found\n"

    def equipArmor(self, armor):
        if self.inventory["Armor"] == []:
            print("\nArmor Is Empty, Can't Equip Armor\n")
            return
        for item in self.inventory["Armor"]:
            if item == armor:
                self.equipedItem["Armor"][armor.split()[1]] = armor
                print(f"\n{armor} successfully Equipped\n")
                for i, y in {
                    "Iron Helmet" : 25, 
                    "Iron Chestplate" : 75,
                    "Iron Leggings" : 50,
                    "Iron Boots" : 15,
                    "Gold Helmet" : 25,
                    "Gold Chestplate" : 75,
                    "Gold Leggings" : 45,
                    "Gold Boots" : 10,
                    "Diamond Helmet" : 50, 
                    "Diamond Chestplate" : 150, 
                    "Diamond Leggings" : 125, 
                    "Diamond Boots" : 25,
                    "Excalibur Helmet" : 200,
                    "Excalibur Chestplate" : 400,
                    "Excalibur Leggings" : 300,
                    "Excalibur Boots" : 100}.items():
                    if armor == i:
                        return y, self.equipedItem["Armor"][armor.split()[1]]
        return "\nArmor not Found\n"


    def useTools(self, tools):
        if self.inventory["Tools"] == []:
            print("\nTools Is Empty, Can't Use Tools\n")
            return
        for item in self.inventory["Tools"]:
            if item == tools:
                print(f"\n{tools} successfully Used\n")
                for i, y in {
                    "Iron Sword" : 100,
                    "Gold Sword" : 75,
                    "Diamond Sword" : 100,
                    "Excalibur Sword" : [500 ,["World Slash", 9999], 100],
                    "Atomic Sword" : [750 ,["Atomic Blast", 99999], 250]}.items():
                    if tools == i:
                        return y
        return f"\n{tools} not Found\n"


    def printEquipedArmor(self):
        print("\n_____Armor_____")
        for i, y in self.equipedItem["Armor"].items():
            print(f"{i}: {y}")


    def printEquipedTool(self):
        print("\n_____Tool_____")
        print(f"{self.equipedItem["Tool"][0]}: {self.equipedItem["Tool"][1]}")


    def printItems(self):
        for value, item in self.inventory.items():
            print(f"{value}:")
            for i in item:
                print(f"    {i}")


    def isMaxInv(self):
        total = 0
        for item in self.inventory.values():
            total += len(item)
        return total >= 50


    def isEmpty(self):
        totalItem = 0
        for item in self.inventory.values():
            totalItem += len(item)
        return totalItem == 0