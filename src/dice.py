import random


class Dice:
    @staticmethod
    def roll():
        dice_number_1 = random.randrange(1, 7)
        dice_number_2 = random.randrange(1, 7)

        return dice_number_1 + dice_number_2
