class MyClass(object):
    'a user-defined wrapper class'
    version = 1.0             # version is a class variable

    def setTo(self, value):    # setTo is a class method
        'sets the instance variable data to value'
        self.data = value      # data is an instance variable

    def get(self):             # get is a class method
        'returns the value of the instance variable data'
        return self.data       # data is an instance variable
    
    def double(self):                   # double is a class method
        'doubles the value of data'
        self.data *= 2

    def ntimes(self, n):
        'multiples data by n'
        self.data *= n

    def __init__(self, val = 1):
        'the constructor'
        self.data = val

    def __repr__(self):
        'the representation'
        return "data = {}".format(self.data)

    def __str__(self):
        'the string format'
        return str(self.data)
