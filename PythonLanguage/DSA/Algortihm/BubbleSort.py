arr_list = [ 2, 3, 5, 4, 1, 7, 6, 8, 9, 10, 15, 12, 14, 11 , 13]

for i in range(len(arr_list) - 1):
    for j in range(len(arr_list) - i - 1):
        if arr_list[j] > arr_list[j + 1]:
            temporary_arr = arr_list[j]
            arr_list[j] = arr_list[j+1]
            arr_list[j+1] = temporary_arr
            print(arr_list)