

def merge(num1, num2, m, n):
    if len(num2) == 0:
        print("Nothing to compare")
        return num1
    pointer1 = m - 1
    pointer2 = n - 1
    last_pointer = m + n - 1
    while pointer1 >= 0 and pointer2 >= 0 :
        print(num1, num2, "Last-Pointer:", last_pointer, "First-Pointer:", pointer1, "Second-Pointer:", pointer2)
        if num1[pointer1] > num2[pointer2]:
            num1[last_pointer] = num1[pointer1]
            pointer1 -= 1
        else:
            num1[last_pointer] = num2[pointer2]
            pointer2 -= 1
        last_pointer -= 1
    num1[:pointer2 + 1] = num2[:pointer2 + 1]

num1 = [1, 2, 3, 0, 0, 0]
num2 = [2, 5, 6]
m = 0
n = len(num2)
for i in num1:
    if i != 0:
        m += 1
result = merge(num1, num2, m, n)
print(num1)
