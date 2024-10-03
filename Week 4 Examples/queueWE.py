# a very simple queue class with exceptions added

class queue(object):
    def __init__(self):
        self.__q = []
    def dequeue(self):
        if self.size() == 0:
            raise EmptyQueue("attempt to dequeue from an empty queue")
        return self.__q.pop(0)
    def enqueue (self, item):
        return self.__q.append(item)
    def size(self):
        return len(self.__q)
    def isEmpty(self):
        return (self.size() == 0)
    def __repr__(self): # for the official string representation of queues
        return self.__q.__repr__()
    def __str__(self): # for the unofficial string representation, like printing queue objects
        return 'none of your business'

    
    def peek(self,key):
        if key >= len(self.__q) or key <0:
            raise BadQueueIndexError()
        return self.__q[key]
    def __getitem__(self, key):
        if key >= len(self.__q) or key <0:
            raise BadQueueIndexError()
        return self.__q[key]
##    def __setitem__(self, key, value):
##        if key >= len(self.__q) or key <0:
##            raise BadQueueIndexError()
##        self.__q[key] = value
    def __iter__(self):
        return iter(self.__q)

class BadQueueIndexError(Exception):
    pass

class EmptyQueue(Exception):
     pass

