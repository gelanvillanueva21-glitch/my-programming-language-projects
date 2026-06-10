
"""
try:
    
    words = ()
    num_of_loop = int(input("Enter Num: "))

    for num in range(num_of_loop):
        word = input("> ")
        every_word = list(words)
        every_word.append(word)
        words = tuple(every_word)
    
    for i in words:
        print(i)


except ValueError:
    print("Wront INPUT!!")

"""
points = ((5, 9, 10), (11, 2, 6), (8, 2, 3))

for w, y, z in points:
    print(w, y, z)