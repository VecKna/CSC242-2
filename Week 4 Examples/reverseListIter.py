class revLstIter(object):
    'the reverse list iterator class'

    def __init__(self, lst):
        'the constructor'
        assert isinstance(lst,list),'This iterator only supports lists'
        #print('INTERATOR CREATED')
        self.__ilst = lst
        self.__index = len(lst) - 1

    def __next__(self):
        'the next method'
        #print('In next-{}'.format(self.__index))
        if self.__index <= -1:
            raise StopIteration()
        val = self.__ilst[self.__index]
        self.__index -= 1

        return val

class revList(list):
    'a reverse list class'

    def __iter__(self):
        return revLstIter(self)
