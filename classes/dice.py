from random import randint

class Dice:
    """An attempt to imitate a dice"""
    def __init__(self, sides):
        self.sides = int(sides)

    def roll_die(self):
        results = []
        print("Now the rolling starts")
        for i in range(10):
            side = randint(1, self.sides)
            results.append(side)
        print(f"10 rolls of {self.sides} sided dice")
        print(results)


my_dice = Dice(10)
your_dice = Dice(6)
her_dice = Dice(20)

my_dice.roll_die()
your_dice.roll_die()
her_dice.roll_die()
