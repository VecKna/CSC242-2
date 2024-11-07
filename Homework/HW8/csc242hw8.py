'''
Authors: William Endres
Collaborators: None
CSC242 Homework 8'''
import os

def wordCount(lst,l, count = 0):
    '''lst = List
    l = letter 
    looks for strings with l in list'''
    assert isinstance(lst,list), 'lst must be a list'
    assert isinstance(l,str), 'l must be a string'
    if len(lst) == 0:
        return count
    if type(lst[0]) == list: #Checks if the first element is a list
        return wordCount(lst[0] + lst[1:],l,count)
        
    if type(lst[0]) == str: #Checks if the first element is a string    
        #searches for letter in string
        if l.lower() in lst[0].lower():
            return wordCount(lst[1:],l,count+1)
        else:
            return wordCount(lst[1:],l,count)
    else:
        return wordCount(lst[1:],l,count)
    

    

                             
print(wordCount([['','cat',12.0,'dog','MOUSE',1,2,'bird',8,9,10]],'o'))
print(wordCount([],'o'))  
print(wordCount([[[['COMPUTER','science',[[4]],[['animation','art']]]]]],'e'))
# see the antivirusredux.py example
def paths(pathname, indent):
    '''Recursively displays all files contained, directly or indirectly, in the folder pathname'''
    #Base Case - empty directory
    if len(os.listdir(pathname)) == 0:
        return
    for items in os.listdir(pathname):
        print(' '*indent,items)
        n = os.path.join(pathname,items)
        if os.path.isdir(n):
            paths(n,indent+2)
        else:
            pass
    #recursive case - directory with files/folders
    #use a for loop just to see whats in the directory

paths('count',4)
paths('/Users/william/Documents/ComputerScience/CSC242-2/Homework/HW8/Test',6)

def sizer(folder):
    pass

print(sizer('Test'))
print(sizer('count'))
print(sizer('Test-2'))           


def uniqueWords(pathname, letter):
    pass

print(uniqueWords('Test','u'))

