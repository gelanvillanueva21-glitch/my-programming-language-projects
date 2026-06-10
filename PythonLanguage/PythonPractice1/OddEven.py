def Odd_Even(input_num):
    if input_num % 2 == 0:
        if input_num == 0:
            print("Your Input Num Is Zero")
        else:
            print(f"{input_num} is An Even number")
    else:
        print(f"{input_num} is An Odd number")
    if input_num > 0:
        print("Your Number Is a Positive")
    elif input_num < 0:
        print("Your Number Is a Negative")

try:
    print("Enter a number")
    input_num = int(input("> "))

    Odd_Even(input_num)
except ValueError:
    print("Input A Number!!")