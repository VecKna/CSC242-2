# A very simple queue class that could use some doc strings

class queue(list):
   
    def dequeue(self):
        return self.pop(0)
    
    def enqueue (self, item):
        return self.append(item)
    
    def size(self):
        return len(self)
    
    def isEmpty(self):
        return (self.size() == 0)

    def sort(self):
        pass

    def reverse(self):
        pass


