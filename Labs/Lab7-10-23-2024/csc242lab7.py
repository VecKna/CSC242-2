'''
CSC242
10-23-2024
Author: William Endres
Aid: N/A
'''
    
def printTriangleManually3():
    print((' ' * 2) + ('*' * 2))
    
def printTriangleManually2():
    print((' ' * 1) + ('*' * 4))
    printTriangleManually3()
    
def printTriangleManually():
    print((' ' * 0) + ('*' * 6))
    printTriangleManually2()

printTriangleManually()

def printTriangleTop(m,i):
    """Recursive function that prints the top of the triangle"""
    if m > 0:
        # 'if num asterisks is 1 or more'
        print((' ' * i ) + ('*' * m))
        printTriangleTop(m - 2,i + 1)
        #print("x"*i)
    if m <= 0:
        #   'If asterisk is 0 or less'
        return

def printTriangleBottom(m,i):
    """Recursive function that utilizes the return to have the print after the call to 
    print from the call before the base case was triggered and then back until the initial call."""
    
    if m <= 0:
        return
    if m > 0:  
        printTriangleBottom(m - 2, i + 1)
        print(" " * i + "*" * m)
        return