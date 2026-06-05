arr_list = [1, 4, 2, 5, 3, 6, 8, 7]

for i in range(1, len(arr_list)):
    j = i
    while arr_list[j - 1] > arr_list[j] and j > 0:
        arr_list[j - 1], arr_list[j] = arr_list[j], arr_list[j - 1]
        j -= 1
print(arr_list)

mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
for i in range(1,n):
    insert_index = i
    current_value = mylist[i]
    for j in range(i-1, -1, -1):
        if mylist[j] > current_value:
            mylist[j+1] = mylist[j]
            insert_index = j
        else:
            break
    mylist[insert_index] = current_value

print(mylist)
