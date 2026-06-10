def mergesort(arr):
    step = 1
    while step < len(arr):
        for i in range(0, len(arr), 2 * step):
            left = arr[i:i + step]
            right = arr[i + step:i + 2 * step]
            merged = merge(left, right)
            for j, val in enumerate(merged):
                arr[i + j] = val
        step *= 2


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and len(right) > j:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr_list = [2, 4, 6, 5, 2, 3, 1, 8, 9, 10]
mergesort(arr_list)
print(arr_list)