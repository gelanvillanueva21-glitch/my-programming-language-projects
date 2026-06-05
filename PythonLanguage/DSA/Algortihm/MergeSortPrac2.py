def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and len(right) > right_index:
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result += left[left_index:]
    result += right[right_index:]
    return result

arr_list = [1, 4, 2, 3, 6, 8, 8, 9]
print(mergesort(arr_list))