
def linear_search(list, result):
    for i in range(0, len(list)):
        if list[i] == result:
            return i
    return None

def verify(index):
    if index is not None:
        print(f"Index {index} Found In The List")
    else:
        print("Index Did Not Found In List")

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = linear_search(number, 10)
verify(result)
result = linear_search(number, 10)
verify(result)