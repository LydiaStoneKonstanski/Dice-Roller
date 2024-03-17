from roll import DieRoller


class MultiDiceRoller:
    def __init__(self):
        pass

        self.roll_again = 'y'
    def roll(self):
        how_many_dice = input("How many dice would you like to roll?")
        for i in range(0,int(how_many_dice)):
            die = DieRoller()
            die.roll_one_die()
    def keep_rolling(self):
        while self.roll_again == 'y':
            self.roll()
            self.roll_again = input("Roll again? (y/n)").lower()

if __name__ == '__main__':
    multi_dice_roller = MultiDiceRoller()
    multi_dice_roller.keep_rolling()