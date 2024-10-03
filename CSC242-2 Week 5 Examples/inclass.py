class revListIter(object):
    def __init__(self, lst):
        assert isinstance(lst,list), 'lst needs to be a list'
        self.__lst=lst
        self.__index=len(lst)-1

    def __next__(self):
        
        if self.__index<=-1:
            raise StopIteration()
        val = self.__lst[self.index]
        self.__index=self.__index-1
        return val
    
class revList(list):
    def __iter__(self):
        