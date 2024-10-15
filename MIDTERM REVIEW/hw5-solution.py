import random
class Die(object):
    def __init__(self,sides):
        assert type(sides)==int, 'sides must be an int'
        self.__sides=sides # indicates a private variable that should not be accesed outside of class
        self.roll()

    def roll(self):
        self.__current = random.randint(1,self.__sides)

    def __str__(self):
        return str(self.__current)
        
    def getValue(self):
        return self.__current

class DieCup(object):
    def __init__(self):
        self.__dieList =[]

    def addDie(self,die):
        assert isinstance(die,Die), 'die must be an instance of a Die class or a class derived from Die'
        self.__dieList.append(die)

    def shake(self):
        for d in self.__dieList:
            d.roll()

    def total(self):
        i=0
        for d in self.__dieList:
            i=i+d.getValue()
        return i
    def __str__(self):
        return f'DieCup has {len(self.__dieList)} items'
    
    def __iter__(self):
        return iter(self.__dieList)
    def __len__(self):
        return len(self.__dieList)
    
class Task(object):
    def __init__(self,name,dueDate=''):
        assert type(name)==str and len(name)>=5, 'text must be string with at least 5 characters'
        assert type(dueDate)==str, 'dueDate must be a string'
        self.__name=name
        self.__dueDate = dueDate

    def getName(self):
        return self.__name
    
    def getDueDate(self):
        return self.__dueDate

    def setDueDate(self,dueDate):
        assert type(dueDate)==str, 'dueDate must be a string'
        self.__dueDate = dueDate

    def __str__(self):
        if len(self.__dueDate)>0:
            return f'{self.__name} is due on {self.__dueDate}'
        else:
            return f'{self.__name} has no specific due date'
    def __repr__(self):
        return f"Task('{self.__name}','{self.__dueDate}')"
        
        
class TodoList(object):
    'The constructor'
    def __init__(self, filename='default.txt'):
        assert type(filename)==str, 'filename must be string'
        self.__filename=filename
        self.__items=[]

    def addItem(self,task):
        'adds an Task to the todo list'
        assert isinstance(task,Task), 'you must add a Task to the TodoList'
        self.__items.append(task)

            
    def removeItem(self, number):
        'removes an Task from the todo list'
        assert type(number)==int, 'number must be an int'
        self.__items.pop(number)

    def __iter__(self):
        'iterates through items in the todo list.'
        return iter(self.__items)

    def __getitem__(self,index):
        assert type(index)==int, 'index must be an int'
        return self.__items[index]

    def __str__(self):
        return f'The todo list has {len(self.__items)} items.'
    def __len__(self):
        return len(self.__items)

    def loadFile(self):
        'loads todo list items from a file.  Existing items in the list are removed'
        self.__items=[]
        try:
            infile = open(self.__filename,'r')
            lines=infile.readlines()
            for line in lines:
                values = line.strip().split(',')
                self.__items.append(Task(values[0],values[1]))
            infile.close()
            return True
        except Exception as e:
            print(e)
            return False
    def saveToFile(self):
        'saves the items to a file.  The file is completely over written'
        try:
            outfile = open(self.__filename,'w')
            for item in self.__items:
                outfile.write(f'{item.getName()},{item.getDueDate()}\n')
            outfile.close()
        except Exception as e:
            print(e)
            return False




    
    
class AverageCalculator(object):
    def __init__(self,fileName='grades.txt'):
        self.filename = fileName
        self.gradeList=[]

    def loadGrades(self):
        try:
            infile = open(self.filename,'r')
            lines = infile.readlines()
            for line in lines:
                grades=[]
                for grade in line.split(','):
                    grades.append(int(grade))
                self.gradeList.append(grades)
            infile.close()
            return True
        except:
            return False


    def writeLetterGrades(self):
        try:
            outfile = open('avg-'+self.filename,'w')
            averages = self.getStudentAverages()
            for avg in averages:
                if avg<=100 and avg>=90:
                    grade='A'
                elif avg<=89 and avg>=80:
                    grade='B'
                elif avg<=79 and avg>=70:
                    grade='C'
                elif avg<=69 and avg>=60:
                    grade='D'
                else:
                    grade='F'
                outfile.write('{}:{}\n'.format(avg,grade))
            outfile.close()
            return True
        except:
            return False

    def getCourseAverage(self):
        averages = self.getStudentAverages()
        return sum(averages)/len(averages)

    def getStudentAverages(self):
        avgList=[]
        for line in self.gradeList:
            avg=sum(line)/len(line)
            avgList.append(avg)
        return avgList
        

class LowestDroppedAverageCalculator(AverageCalculator):
    def __init__(self, fileName='grades.txt'):
        AverageCalculator.__init__(self,fileName)

    def getStudentAverages(self):
        avgList=[]
        for line in self.gradeList:
            lowest= min(line)
            avg=(sum(line)-lowest)/(len(line)-1)
            avgList.append(avg)
        return avgList
        
    
