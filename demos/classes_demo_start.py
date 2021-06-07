import random

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

        # We can use the `spot` variable to correctly registed this person at their correct spot in
        # `line` by storing this object (self) in line[spot]. 
        line[spot] = self
    
    def show(self):
        print(self.name + str(self.starting_spot))

def show_line():
    for person in line:
        if person is not None:
            person.show()
        else:
            print('None')


# Above ^^^ has the useful code you should look for to draw parallels to the chess game
# ------------------------------------------------------------------------------------
# Below vvv has the code that is just there to make the demo run. It can also be a good refrence,
# but is less directly relevent to chess. 
            
        
# Main function, demoing the line
def main():
    
    for spot in range(20): # for spot in [0,1,...,19]:
        Person(spot) # Create a new spot object, which runs the __init__ method

    # Show the list
    print('showing the line:')
    show_line()

    # See what's actuall in the line (the Person object objects)
    print('\nprinting the line directly:')
    print(line)
    
        

# If this is the file we are running directly, then run the main() function.
if __name__ == '__main__': 
    main()
