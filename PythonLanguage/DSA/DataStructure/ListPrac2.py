new_List = []
new_List.extend([1, 2, 3, 4, 5, 6, 7, 8])

print(new_List)
num = new_List.copy()
num = list(num)

for i in num:
    if i == 2:
        num.remove(2)
    print(i)