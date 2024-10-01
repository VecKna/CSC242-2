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
        print('data = ',self.data)
