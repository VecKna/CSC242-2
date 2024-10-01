import random
class Die(object):
    'a class representing a Die'

    def __init__(self, sides = 6):
        'The constructor of the Die'
        self.sides = sides

    def roll(self):
        'roll the dice using random'
        self.rolled = random.randint(1, self.sides)
        
    def get(self):
        'get the current value of the die'
        return self.rolled

    def numSides(self):
        'get the number of sides of the die'
        return self.sides

    def __repr__(self):
        'The representation of the object that returns the amount of sides'
        return f'Die({self.sides})'

    def __str__(self):
        'The string representation of the class'
        return f"'{self.sides}'"


    

def rollDice(rolls, sides):
    '''A function that rolls dice'''
    #initializes the Die class
    d1 = Die(sides)
    d2 = Die(sides)
    for i in range(0, rolls):
        d1.roll()
        d2.roll()
        print(f'Roll {i} : {d1.get()} - {d2.get()}')
        



        
   
        
