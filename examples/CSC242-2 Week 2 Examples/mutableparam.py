def g(lst):
    print("In g, before assignment")
    print("id(lst) (in g) = ", id(lst))
    print("id(lst[0]) (in g) = ", id(lst[0]))
    lst[0] = 5
    print("In g, after assignment")
    print("id(lst) (in g) = ", id(lst))
    print("id(lst[0]) (in g) = ", id(lst[0]))

def f():
    lst = [3, 6, 9, 12]
    print("In f, before call to g")
    print("id(lst) (in f) = ", id(lst))
    print("id(lst[0]) (in f) = ", id(lst[0]))
    g(lst)
    print("In f, after call to g")
    print("id(lst) (in f) = ", id(lst))
    print("id(lst[0]) (in f) = ", id(lst[0]))
