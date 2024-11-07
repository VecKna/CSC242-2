def flattenListWithPrint(lst):
    localLst=[]
    if len(lst)==0:
        return []
    if type(lst[0])==list:
        sublist = flattenListWithPrint(lst[0])
        localLst += sublist
    else:
        print(lst[0])
        localLst.append(lst[0])
    return localLst + flattenListWithPrint(lst[1:])


def listPrint(lst):
    if len(lst)==0:
        return
    if type(lst[0])==list:
        listPrint(lst[0])
    else:
        print(lst[0])
    listPrint(lst[1:])

l=[1,2,3,4]
l2=[[1,2],[3,4],[4,5]]
l3=[1,2,[3,4,[5,6]],7,8,[[[[[[9]]]]]]]


def printLst(lst):
    if len(lst) == 0:
        return
    else:
        print(lst[0])
        printLst(lst[1:])

