import random as r


class Dice:
    def roll(self, guess):
        result_roll = r.randint(1, 5)
        if guess == result_roll:
            print("Correct Guess!")
            return False
        else:
            print('Wrong Guess')
            return True
            


dice = Dice()
Stop_Continue = True
while Stop_Continue:
    try:
        guess = int(input("> "))
    except ValueError:
        print("ENTER A NUMBER!!")
        continue
    Stop_Continue = dice.roll(guess)
