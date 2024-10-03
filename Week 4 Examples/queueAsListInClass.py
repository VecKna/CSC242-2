class queue(list):
    'a queue class'

    # self is an empty list
##    def __init__(self):
##        'the constructor'
##        self.q = []

    def enqueue(self, item):
        'add an item to the back of the queue'
        self.append(item)

    def dequeue(self):
        'remove and return the front item'
        return self.pop(0)

    def size(self):
        'return the number of items in the queue'
        return len(self)

    def isEmpty(self):
        'returns True if the queue is empty, False ow'
        if self.size() == 0:
            return True
        else:
            return False

    # already defined for lists
##    def __repr__(self):
##        'the representation'
##        return str(self.q)

    def __str__(self):
        'a pretty representation'
        return "The queue currently is:{}".format(repr(self))

    def sort(self):
        pass

    # already defined
##    def __iter__(self):
##        'the iterator'
##        return iter(self.q)
