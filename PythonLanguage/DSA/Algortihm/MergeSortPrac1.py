def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    rightHalf = arr[:mid]
    leftHalf = arr[mid:]
    sortRight = mergeSort(rightHalf)
    sortLeft = mergeSort(leftHalf)
    return merge(sortLeft, sortRight)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and len(right) > j:
        if left[i] < right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


arr_list = [1, 4, 2, 5, 6, 3, 7, 9, 8]
print(mergeSort(arr_list))