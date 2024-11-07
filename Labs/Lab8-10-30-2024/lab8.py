#def extractStr(lst):
#    '''extractStr(lst) -> str'''
 #   if not lst:
  #      return ''
    
   # if isinstance(lst[0], str):
    #    return lst[0] + extractStr(lst[1:])
   # elif isinstance(lst[0], list):
    #    return extractStr(lst[0]) + extractStr(lst[1:])
    #else:
    #    return extractStr(lst[1:])
    #

def extractStr(lst):
    'Extacts strings from an arbitrarily nested list'
    localLst = []
    if len(lst) == 0:
        return ''
    if type(lst[0]) == list:
        sublist = extractStr(lst[0])
        localLst += sublist
    if type(lst[0]) == str:  
        print(lst[0])
        localLst.append(lst[0])
    if type(lst[0]) == int or type(lst[0]) == float:
        pass  # or any other appropriate action for int or float types
    
    return localLst + extractStr(lst[1:])
def totalNumericValue(lst):
    'totals integers from an arbitrarily nested list'
    
    pass
