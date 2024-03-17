# roll a "die" some number of times.
from random import randint

class DieRoller:

    def __init__(self):
        self.roll_again = 'y'
    def roll_one_die(self)->int:
        die_value = randint(1, 6)
        print(die_value)

    def keep_rolling(self):
        while self.roll_again == 'y':
            self.roll_one_die()
            self.roll_again = input("Roll again? (y/n)").lower()

if __name__ == '__main__':
    die = DieRoller()
    die.keep_rolling()


# roll - run it once and go into a loop
# roll 1 - produce a number 1-6 random and print it
# roll 2 - produce two numbers 1-6 and print them
# roll 3 - produce three numbers and print them.
#

