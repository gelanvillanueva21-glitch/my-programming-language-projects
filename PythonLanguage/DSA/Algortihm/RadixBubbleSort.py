def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def radixsort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        radixList = [[], [], [], [], [], [], [], [], []]
        for num in arr:
            radixIndex = (num // exp) % 10
            radixList[radixIndex].append(num)
        for bucket in radixList:
            bubblesort(bucket)
        i = 0
        for bucket in radixList:
            for num in bucket:
                arr[i] = num
                i += 1
        print(radixList)
        exp *= 10



arr_list = [13, 34, 12 ,55, 14, 26, 48, 17]
radixsort(arr_list)
print(arr_list)