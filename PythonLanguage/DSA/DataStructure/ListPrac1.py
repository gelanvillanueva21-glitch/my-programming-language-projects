numbers = [2, 2, 4, 4, 1, 3, 1, 4, 3, 5, 6, 7, 5, 6, 7, 8, 3]

try:
    target = int(input("> "))
    count1 = 0
    count2 = 0

    for num in numbers:
        if num != target:
            count2 += 1
        else:
            count1 += 1
    print(f"You found the number {target}, {count1} times,\nyou check the numbers {count2} times")
except ValueError:
    print("Wrong Input")