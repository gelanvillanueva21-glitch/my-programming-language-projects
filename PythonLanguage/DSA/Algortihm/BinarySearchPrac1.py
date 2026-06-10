def binary_search(numbers, target):
    first = 0
    last = len(numbers) - 1

    while first <= last:
        mid_point = (first + last) // 2

        if numbers[mid_point] == target:
            return True
        elif numbers[mid_point] < target:
            first = mid_point + 1
        else:
            last = mid_point - 1
        
    return None

numbers = [6,7,8,9,10,11,12,13,14,15]
print(binary_search(numbers, 12))