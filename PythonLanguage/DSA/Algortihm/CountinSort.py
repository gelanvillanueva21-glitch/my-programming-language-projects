
def countingsort(array):
    max_val = max(array)
    count = [0] * (max_val + 1)

    while len(array) > 0:
        num = array.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            array.append(i)
            count[i] -= 1
    return array


arr_list = [1 ,4 ,2 ,6 ,7, 5, 3, 4, 2, 1, 2, 5]
print(countingsort(arr_list))