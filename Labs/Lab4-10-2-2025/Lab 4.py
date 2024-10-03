"""
CSC 242
Lab 4 
Author: William Endres
Collaborators: Patrick (he helped me debug mean())
"""

class Stat(object):
    '''Stat class
    parent: object
    arguments: none or a list'''
    def __init__(self, ls = []):
        assert type(ls) == list, 'Parameter must be a list'
        self.ls = ls

    def add(self, num):
        """Takes in an integer or float and appends
        to self.ls
        Args:
            num (int or float)
        """
        assert int(num) or float(num), 'Paremeter must be a float or an int'
        self.ls.append(num)

    def sum(self):
        '''loops through the list and calculates the sum'''
        if len(self.ls) == 0:
            return 0.0
        else:
            sum = 0
            for i in range(len(self.ls)):
                sum += self.ls[i]
            return sum
    
    def max(self):
        '''Returns the highest value number in the list'''
        if len(self.ls) == 0:
            return 0.0
        else:
            maxValue = self.ls[0]
            for j in self.ls:
                if j > maxValue: 
                    maxValue = j
            return maxValue
        
        
    def min(self):
        '''Returns the number with the least value in the list'''
        if len(self.ls) == 0:
            return 0.0
        else:   
            minValue = self.ls[0]
            for j in self.ls:
                if j < minValue:
                    minValue = j
            return minValue

    def clear(self):
        'Clears the list by setting it equal to an empty list'
        self.ls = []

    def mean(self):
        '''Sums the list then divides 
        by number of objects in set'''
        if len(self.ls) == 0:
            return 0.0
        else:
            return sum(self.ls)/len(self.ls)
    
    def __str__(self):
        'Person friendly description of the object'
        return f'Stat object with {len(self.ls)} items.'
    
    def __repr__(self):
        'Code friendly representation of the object'
        return f'Stat({self.ls})'
    
    def __eq__(self, other): 
        '''Custom equality method that checks if other object is a Stat object then compares the
        sum of both'''
        if isinstance(other, Stat):
            return sum(self.ls) == sum(other.ls)
           

