class queue(object):
    'a queue class'

    def __init__(self):
        'the constructor'
        self.__q = []

    def enqueue(self, item):
        'add an item to the back of the queue'
        self.__q.append(item)

# define a queue exception class
# modifiy dequeue to use it

    def dequeue(self):
        'remove and return the front item'
##        try:
##            return self.q.pop(0)
##        except:
##            raise DequeueExcept("Cannot dequeue from an empty queue")
        
        if self.size() > 0:
            return self.__q.pop(0)
        else:
            raise DequeueExcept("Cannot dequeue from an empty queue")

    def size(self):
        'return the number of items in the queue'
        return len(self.__q)

    def isEmpty(self):
        'returns True if the queue is empty, False ow'
        if self.size() == 0:
            return True
        else:
            return False

    def __repr__(self):
        'the representation'
        return str(self.q)

    def __str__(self):
        'a pretty representation'
        return "The queue currently is:{}".format(self.__q)

    def __iter__(self):
        'the iterator'
        return iter(self.__q)

class QException(Exception):
    def __init__(self, val = ''):
        self.v = val
    def __str__(self):
        return str(self.v)

class DequeueExcept(QException):
    pass
