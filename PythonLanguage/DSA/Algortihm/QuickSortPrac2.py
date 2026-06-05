
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i+1


def quicksort(array, low = 0, high = None):
    if high is None:
        high = len(arr_list) - 1

    if low < high:
        print(array)
        pivot = partition(array, low, high)
        quicksort(array, low, pivot - 1)
        quicksort(array, pivot + 1, high)


arr_list = [21, 54, 87, 34, 35, 68, 12]
quicksort(arr_list)
print(arr_list)