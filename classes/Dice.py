import random


class Dice:
    def roll(self):
        die = (random.randint(1, 6), random.randint(1, 6))
        print(die)


die1 = Dice()
die1.roll()
