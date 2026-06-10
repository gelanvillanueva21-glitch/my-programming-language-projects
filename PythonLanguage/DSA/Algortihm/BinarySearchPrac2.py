
def binarySearch(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        print(mid)
    return -1

num = [2, 3, 4, 6, 8, 9, 11, 23, 43, 64]
print(binarySearch(num, 64))