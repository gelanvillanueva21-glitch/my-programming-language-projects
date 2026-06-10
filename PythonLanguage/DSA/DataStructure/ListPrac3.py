def sum_index(numbers, target):
    index = 0

    while True:
        for i in range(len(numbers)):
            if (numbers[index] + numbers[i]) == target:
                index_num = [index, i]
                return index_num
        index += 1

numbers = [12, 2, 5, 6, 10]
target = 15
print(f"Index: {sum_index(numbers, target)}")
print(f"Target: {target}")