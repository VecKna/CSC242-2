import random
class Die(object):
    'a class representing a Die'

    def __init__(self, sides = 6):
        'The constructor of the Die'
        assert int(sides), 'amount of sides is not an integer'
        self.sides = sides
        self.rolled = 0

    def roll(self):
        'roll the dice using random'
        self.rolled = random.randint(1, self.sides)
        
    def get(self):
        'get the current value of the die'
        if self.rolled == 0:
            return 'Roll the die first!'
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
    d1 = Die(sides)
    d2 = Die(sides)
    for i in range(0, rolls):
        d1.roll()
        d2.roll()
        print(f'Roll {i} : {d1.get()} - {d2.get()}')


class Person(object):
    '''A class that represents a person'''

    def __init__(self, name = 'John Doe', age = 0, weight = 1):
        'The initializer for the Person class.' 
        assert str(name) and len(name) > 0, 'Name must be a string with a length greater than zero'
        assert (type(weight) == int or type(weight) == float), f'Please enter a valid number'
        assert int(age), f'please enter a valid integer'
        assert age >= 0, f'Age must be greater than or equal to zero' 
        assert weight > 0, f'Weight must be a number with a value greater than 0'
        self.name = name
        self.weight = weight
        self.age = age

    def increaseWeight(self, weight):
        'A method that will add to the current weight of the '
        assert (type(weight) == int or type(weight) == float), f'Please enter a valid weight greater than zero'
        self.weight += weight

    def __repr__(self):
        'returns a string containing Person and the three parameters'
        return f'Person({self.name},{self.age},{self.weight})'

    def __str__(self):
        'returns a string containing the three parameters passed in'
        return f'{self.name} is age {self.age} and weighs {self.weight} pounds.'
        



        
        
   
        
