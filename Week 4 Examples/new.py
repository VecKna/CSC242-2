##class Bad(Exception):
##    def __init__(self, value = ''):
##        self.v = value
##    def __str__(self):
##        return str(self.v)

### Alternate definition
class BadError(Exception):
    pass

def doomed():
    raise BadError("Sugar is bad for you!")

def doomed2():
    try:
        doomed()
    except BadError as e:
        print("Caught Bad in  doomed2(): ", e)
        #raise
##try:
##    doomed2()
##except Bad:
##    print("Caught Bad")
##    raise
##print("Last line")
