def sums(lst):

    if len(lst) == 0:
        return 0
    #what is the recursive step?
    if type(lst[0]) == int or type(lst[0]) == float:
        return lst[0] + sums(lst[1:])
    if type(lst[0]) == list:
        return sums(lst[0]) + sums(lst[1:])
    else:
        return sums(lst[1:])

#print(sums([1,2,3,4,5]))
#print(sums([[[[[1]]]],2,[3,4],5]))

    
import os

def count(pathname, name):
    'Count folders with name in pathname'
    i = 0
    for item in os.listdir(pathname):
        n = os.path.join(pathname, item)
        if os.path.isdir(n):
            print('n:',n)
            print("item:",item)
            if item.lower() == name.lower():
                i += 1 
            i = i + count(n, name)
    return i
    #recursive case - directory with files/folders
 
count('count','A')