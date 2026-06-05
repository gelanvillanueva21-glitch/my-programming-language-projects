import DropChance as chance

rand_chance = chance.Chance()
result = rand_chance("Easy")
num = 0
list_item = []
rare_item = []
while num != 10000:
    num += 1
    item = result()
    if item in ["Excalibur Helmet", "Excalibur Chestplate", "Excalibur Leggings", "Excalibur Boots", "Excalibur Sword", "Atomic Sword"]:
        rare_item.append(item)
    elif item is not None:
        list_item.append(item)
print(list_item)
print(len(rare_item))
print(len(list_item))