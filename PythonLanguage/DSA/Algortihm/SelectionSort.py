arr_list = [2, 4, 1, 3, 7, 9, 8, 5]

for i in range(len(arr_list) - 1):
    min_index = i
    for j in range(i + 1, len(arr_list)):
        if arr_list[j] < arr_list[min_index]:
            min_index = j
    arr_list[i], arr_list[min_index] = arr_list[min_index], arr_list[i]
print(arr_list)

mylist = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(mylist)
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if mylist[j] < mylist[min_index]:
            min_index = j
    min_value = mylist.pop(min_index)
    mylist.insert(i, min_value)

print(mylist)
