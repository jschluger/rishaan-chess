
#### How to view & run this notebook:
1. View it on github at https://github.com/jschluger/rishaan-chess/blob/main/final_notes.md
2. To run the notebook, install Anaconda here, https://docs.anaconda.com/anaconda/install/index.html, then use that to run jupyter notebook.
----

# Part One: Chess Game

To implement our virtual chess game, we split the game into several classes to represent the different parts of the game. The major different parts of the game we had to represent were:
1. The underlying logic of the game of chess, and data about the current state of the game as its played.
2. The front end display which gives the user a visual representation of logical game represented in part 1. 

To represent part 1, we wrote the chess.ChessGame class (in chess.py); this stores the board state in a 2D-array of chess.LogPiece instances (or None). 

To acomplish part 2, we wrote the play_chess_graphics.py script. This uses an instance of chess.ChessGame to manage the chess game, while also using pygame directly, and instances of our play_chess_graphics.Piece class to display the game visually. We wrote a main() function to setup the board and start the game, and actually playing the game happens in play_turn()

Finally, we later built the Wireless class to control all the network connection code and enable us to develop the remote two player version of the game. 

# Part Two: Coding tools

### Classes
We use classes to package specific parts of a program into one neat and tidy place to easily use them later.

E.g.:


```python
class MyClass():
    
    # All classes need an __init__ to setup the class
    def __init__(self, name):
        super().__init__()
        
        # self.name is an instance variable
        self.name = name
        
    # This is a regular class method; you can call the method from absany instance of the class
    def get_name(self):
        return self.name
    
myInstance = MyClass('Rishaan')
# myInstance is an instance of MyClass because we used parenthies to construct an instance of MyClass (with name=Rishaan)

# We can confirm with the isinstance method:
print(isinstance(myInstance, MyClass))
        
```

    True


###  Copying data

We saw how it is possible to modify the contents of one variable from another when there are multiple refrences to the same data in a program:


```python
print('Simple example\n------------------------')
L = [0,1,2,3,4,5,6,7,8,9]
L2 = L
print('L = ',L)
print('L2 = ',L2)

print('\nmodifying L2...')
L2[0] = 'changed in L2'
print('L = ',L)
print('L2 = ',L2)

print('\nMore complicated example\n------------------------')
A = ['A','B','C']
X = ['X','Y','Z']
M = [A,X]
print('A = ',A)
print('X = ',X)
print('M = ',M)

print('\nmodifying A')
A[0] = 'changed in A'

print('A = ',A)
print('X = ',X)
print('M = ',M)

print('\nmodifying M')
M[1][0] = 'changed in M'

print('A = ',A)
print('X = ',X)
print('M = ',M)

```

    Simple example
    ------------------------
    L =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    L2 =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    modifying L2...
    L =  ['changed in L2', 1, 2, 3, 4, 5, 6, 7, 8, 9]
    L2 =  ['changed in L2', 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    More complicated example
    ------------------------
    A =  ['A', 'B', 'C']
    X =  ['X', 'Y', 'Z']
    M =  [['A', 'B', 'C'], ['X', 'Y', 'Z']]
    
    modifying A
    A =  ['changed in A', 'B', 'C']
    X =  ['X', 'Y', 'Z']
    M =  [['changed in A', 'B', 'C'], ['X', 'Y', 'Z']]
    
    modifying M
    A =  ['changed in A', 'B', 'C']
    X =  ['changed in M', 'Y', 'Z']
    M =  [['changed in A', 'B', 'C'], ['changed in M', 'Y', 'Z']]


So, when we don't want this behavior we can use copy and deepcopy to get seperate copies of the same data.


```python
from copy import copy, deepcopy

print('Simple example with copy\n------------------------------')
L = [0,1,2,3,4,5,6,7,8,9]
L2 = copy(L)
print('L = ',L)
print('L2 = ',L2)

print('\nmodifying L2...')
L2[0] = 'changed in L2'
print('L = ',L)
print('L2 = ',L2)

print('\nMore complicated example with copy (note how it doesn\'t work)\n-----------------------------')
A = ['A','B','C']
X = ['X','Y','Z']
M = copy([A,X])
print('A = ',A)
print('X = ',X)
print('M = ',M)

print('\nmodifying A')
A[0] = 'changed in A'

print('A = ',A)
print('X = ',X)
print('M = ',M)

print('\nmodifying M')
M[1][0] = 'changed in M'

print('A = ',A)
print('X = ',X)
print('M = ',M)

print('\nMore complicated example with deepcopy\n--------------------------------')
A = ['A','B','C']
X = ['X','Y','Z']
M = deepcopy([A,X])
print('A = ',A)
print('X = ',X)
print('M = ',M)

print('\nmodifying A')
A[0] = 'changed in A'

print('A = ',A)
print('X = ',X)
print('M = ',M)

print('\nmodifying M')
M[1][0] = 'changed in M'

print('A = ',A)
print('X = ',X)
print('M = ',M)
```

    Simple example with copy
    ------------------------------
    L =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    L2 =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    modifying L2...
    L =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    L2 =  ['changed in L2', 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    More complicated example with copy (note how it doesn't work)
    -----------------------------
    A =  ['A', 'B', 'C']
    X =  ['X', 'Y', 'Z']
    M =  [['A', 'B', 'C'], ['X', 'Y', 'Z']]
    
    modifying A
    A =  ['changed in A', 'B', 'C']
    X =  ['X', 'Y', 'Z']
    M =  [['changed in A', 'B', 'C'], ['X', 'Y', 'Z']]
    
    modifying M
    A =  ['changed in A', 'B', 'C']
    X =  ['changed in M', 'Y', 'Z']
    M =  [['changed in A', 'B', 'C'], ['changed in M', 'Y', 'Z']]
    
    More complicated example with deepcopy
    --------------------------------
    A =  ['A', 'B', 'C']
    X =  ['X', 'Y', 'Z']
    M =  [['A', 'B', 'C'], ['X', 'Y', 'Z']]
    
    modifying A
    A =  ['changed in A', 'B', 'C']
    X =  ['X', 'Y', 'Z']
    M =  [['A', 'B', 'C'], ['X', 'Y', 'Z']]
    
    modifying M
    A =  ['changed in A', 'B', 'C']
    X =  ['X', 'Y', 'Z']
    M =  [['A', 'B', 'C'], ['changed in M', 'Y', 'Z']]


### Working with data in lists
We learned about fast ways to work with data in lists:

#### Filter: Keep/remove items from a list based on a function of each item
e.g.:


```python
N = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

# Iterate through only the even numbers in N:
for x in filter(lambda x: x % 2 == 0, N):
    print(x)
    
# Or, to get these numbers as a list:
even_N = list(filter(lambda x: x % 2 == 0, N))
print(even_N)
```

    0
    2
    4
    6
    8
    10
    12
    14
    16
    18
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


#### Map: transform one list into another list by using a fuction to transform each element:
e.g.:


```python
M = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

def foo(x):
    if x % 2 == 0:
        return x
    else:
        return -1 * x
    
# Or, to get these numbers as a list:
new_M = list(map(foo, M))
print(new_M)
```

    [0, -1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16, -17, 18, -19]

