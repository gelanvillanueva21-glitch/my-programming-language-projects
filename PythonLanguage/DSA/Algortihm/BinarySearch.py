def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        mid_point = (first + last)//2

        if list[mid_point] == target:
            return mid_point
        elif list[mid_point] < target:
            first = mid_point + 1
        else:
            last = mid_point - 1
    return None

def verify(index):
    if index is not None:
        print(f"Index {index} Found In The List")
    else:
        print("Index Did Not Found In List")

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = binary_search(number, 9)
verify(result)
result = binary_search(number, 10)
verify(result)