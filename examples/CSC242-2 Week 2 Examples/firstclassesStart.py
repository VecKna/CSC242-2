class MyClass(object):
    '''a user-defined wrapper class'''

 
    def setTo(self, value):    # setTo is a class method
        'sets the instance variable data to value'
        self.data = value      # data is an instance variable
        
    def get(self):             # get is a class method
        'returns the value of the instance variable data'
        return self.data       # data is an instance variable

