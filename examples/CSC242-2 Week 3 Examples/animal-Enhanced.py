class Animal(object):
    'a class that abstracts an animal'
    def __init__(self, s = 'default', l = 'default'):
        self.species = s
        self.language = l
        self.sleeping=False
        
    def setSpecies(self, name):
        'sets the species of the animal'
        self.species = name
        
    def setLanguage(self, lang):
        'sets the language of the animal'
        self.language = lang
        
    def speak(self):
        'ask the animal to speak if they are awake'
        if self.sleeping==True:
            return "Zzzzzzzzzz...."
        else:
            return 'I am a {} and I {}'.format(self.species, self.language)

    def sleep(self):
        'put the animal to sleep'
        self.sleeping=True
        return 'I am sleeping'

    def awake(self):
        'awaken the animal'
        self.sleeping=False
        return 'I am awake'

    def __eq__(self, other):
        'check if two animals are the same'
        return self.species.lower() == other.species.lower() and self.language == 	other.language

 
    def __mul__(self,copies):
        'make clones of an animal'
        clones=[]
        for i in range(copies):
            clones.append(eval(repr(self)))
        return clones
    
    def __repr__(self):
        'get the python representation of the animal'
        return "Animal('{}', '{}')".format(self.species, self.language)

    def __str__(self):
        'get the string representation of the animal'
        return self.speak()

    def __add__(self, other):
        'create a hybrid animal'
        return Animal(self.species+"/"+other.species, self.language+"/"+other.language)

class Bird(Animal):
    'a class that extends Animal for a bird'
    
    def fly(self, n):
        '''returns a message about the height of flight.
            Notice only birds, not animals can fly. '''
        if self.sleeping==False:
            return 'I am flying {} feet!'.format(n)
        else:
            return 'I am sleeping! Leave me alone!'

    def __init__(self,lang='chirp'):
        'Bird constructor. Calls into the Animal constructor'
        Animal.__init__(self,'bird',lang)

    def __repr__(self):
        'Bird representation'
        return "Bird('{}')".format(self.language)
