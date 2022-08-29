from ast import expr_context
import copy
from importlib.resources import contents
import random
# Consider using the modules imported above.

# Variable-length arguments
# *args: for non-keyworded/positional arguments
# **kwargs: for keyworded arguments
# *args and **kwargs, represent the iterables that would be accessed during a function call

class Hat:

    contents = [] # type List

    def __init__(self, **balls): # balls = type Dict
        
        self.contents = []

        for key, value in balls.items():
            
            i = 0
            while i < value:
                self.contents.append(key) # Inserting balls in Hat
                i += 1
    
    def draw(self, num):

        if num > len(self.contents):
            num = len(self.contents)

        extraction = []
        
        i = 0
        while i < num:
            b = random.randint(0, len(self.contents)-1)
            removed = self.contents.pop(b)
            extraction.append(removed) # Remove item from content list + Insert in extraction list
            i += 1
        
        return extraction

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    start_balls = hat.contents.copy()
    start_expec = expected_balls.copy()
    success = 0

    t = 0
    while t < num_experiments: # experiment 1, 2, ...

        hat.contents = start_balls.copy() # each experiment has same starting hat content
        expected_balls = start_expec.copy()
        extracted_balls = []

        extracted_balls = hat.draw(num_balls_drawn) # extraction

        for color, times in expected_balls.items(): # checking expectations
            for i in extracted_balls:
                if i == color: # if an extracted ball is present in expected balls, then count it
                    expected_balls[color] -= 1

        if all(value <= 0 for value in expected_balls.values()): # if all expectations are met, then success
            success += 1
        
        t +=1
    
    return success / num_experiments # proportion