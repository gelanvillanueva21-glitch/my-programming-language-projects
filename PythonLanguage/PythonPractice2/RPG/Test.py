import DropChance as chance

rand_chance = chance.Chance()
result = rand_chance("Easy")
num = 0
list_item = []
rare_item = []
item = result()
if item:
    if item[1] is not None:
        print(item)