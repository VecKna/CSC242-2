from SafeAnimal import Animal, Bird        

class Zoo(object):
    def __init__(self):
        self.__animals=[]

    def addAnimal(self,animal):
        assert isinstance(animal,Animal), 'You can only add types derived by Animal to the zoo.'
        self.__animals.append(animal)

    def speakAll(self):
        for animal in self.__animals:
            print(animal.speak())

    def sleepAll(self):
        for animal in self.__animals:
            print(animal.sleep())

    def awakeAll(self):
        for animal in self.__animals:
            print(animal.awake())

    def releaseAnimals(self):
        self.__animals.clear()
    

    def __getitem__(self,index):
        assert type(index)==int, 'Index must be an int'
        return self.__animals[index]

    def __iter__(self):
        return iter(self.__animals)
