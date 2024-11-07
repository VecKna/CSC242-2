
def printLineWithSum(num):
    if num <=0:
        return 0
    else:
        retVal = printLineWithSum(num//10)
        localVal = num%10
        print (localVal)
        return localVal + retVal

print(printLineWithSum(1234))

def printLineWithList(num):
    if num <=0:
        return []
    else:
        retVal = printLineWithList(num//10)
        localVal = num%10
        print (localVal)
        retVal.append(localVal)
        return retVal

print(printLineWithList(5678))
