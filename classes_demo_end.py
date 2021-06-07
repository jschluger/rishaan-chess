import random
import unittest

# The possible names to pick from
name_choices = ['Olivia', 'Emma', 'Ava', 'Sophia', 'Isabella', 'Charlotte', 'Amelia', 'Mia', 'Harper', 'Evelyn', 'Abigail', 'Emily', 'Ella', 'Elizabeth', 'Camila', 'Luna', 'Sofia', 'Avery', 'Mila', 'Aria', 'Scarlett', 'Penelope', 'Layla', 'Chloe', 'Victoria', 'Madison', 'Eleanor', 'Grace', 'Nora', 'Riley', 'Zoey', 'Hannah', 'Hazel']

# The datastructure representing the line.
# The line has 20 spots in it, and it starts out totally empty: with no one in each spot.
line = [None] * 20

# A class representing 
class Person():
    # While initilizing a person, we know what spot in line they are currently located at
    # because we get the `spot` argument in the __init__ function.
    def __init__(self, spot):
        self.name = random.choice(name_choices)
        self.spot = spot
        self.starting_spot = spot
        self.cheers_done = 0

        # We can use the `spot` variable to correctly registed this person at their correct spot in
        # `line` by storing this object (self) in line[spot]. 
        line[spot] = self
    
    def show(self):
        print(self.name)
        self.cheer()
        print(f'\t(started at {self.starting_spot}, has cheered {self.cheers_done} times)')



class EvenFan(Person):
    def __init__(self,spot):
        super().__init__(spot)

    def cheer(self):
        print('\tGo Evens!')
        self.cheers_done += 1

class OddFan(Person):
    def __init__(self,spot):
        super().__init__(spot)

    def cheer(self):
        print('\tThe Odds are the best!')
        self.cheers_done += 1


def show_line():
    print('-----------------------------')
    for person in line:
        if person is not None:
            person.show()
        else:
            print('None')
    print('-----------------------------')


# Above ^^^ has the useful code you should look for to draw parallels to the chess game
# ------------------------------------------------------------------------------------
# Below vvv has the code that is just there to make the demo run. It can also be a good refrence,
# but is less directly relevent to chess. 
            
        
# Main function, demoing the line
def main():
    for spot in range(len(line)): # for spot in [0,1,...,19]:
        if spot % 2 == 0:
            EvenFan(spot) # Create a new spot object, which runs the __init__ method
        else:
            OddFan(spot) # Create a new spot object, which runs the __init__ method

    # Show the list
    print('showing the line:')
    show_line()

    p = line[10]
    print('line[10], has type',type(p))
    p.show()
    p.show()
    for i in range(10):
        p.cheer()
    p.show()
    assert p.cheers_done == 13

class MySkippedTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual()
# If this is the file we are running directly, then run the main() function.
if __name__ == '__main__': 
    main()
