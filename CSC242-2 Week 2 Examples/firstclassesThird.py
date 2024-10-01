class MyClass(object):
    'a user-defined wrapper class'

    def setTo(self, value):    # setTo is a class method
        'sets the instance variable data to value'
        self.data = value      # data is an instance variable

    def get(self):             # get is a class method
        'returns the value of the instance variable data'
        return self.data       # data is an instance variable

class My2ndClass(MyClass):              # inherits attributes from MyClass
    'a subclass of MyClass'
    
    def double(self):                   # double is a class method
        'doubles the value of data'
        self.data *= 2
        
    def get(self):                      # get is an overridden class method
        'prints the value of data'
        print('data =',self.data)

class My3rdClass(My2ndClass):           # inherits attributes from My2ndClass
    'augments 2nd class with constructor, add and mul operators'
    
    def __init__(self, value = 0):          # overridden constructor
        'overloaded constructor'
        self.data = value
        
    def __add__(self, other):           # overloaded add operator
        'overloads the add operator'
        return My3rdClass(self.data + other.data)
    
    def __mul__(self, other): # overloaded mul operator
        'overloads the mul operator'
        return My3rdClass(self.data * other.data)
