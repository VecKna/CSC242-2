class Animal(object):
    'a class that abstracts an animal'
    def __init__(self, s = 'default', l = 'default'):
        assert type(s) == str and len(s) > 0, f'{s} is not a string or empty'
        assert type(l) == str, f'{s} is not a string'
        self.species = s
        self.language = l
        self.sleeping=False
        
    def setSpecies(self, name):
        assert type(name) == str and len(name) > 0, f'{name} is not a string or empty'
        'sets the species of the animal'
        self.species = name
        
    def setLanguage(self, lang):
        assert type(lang) == str and len(lang) > 0, f'{lang} is not a string or empty'
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
        assert type(other) == Animal, f'You can only compare to another anmial'
        
        return self.species.lower() == other.species.lower() and self.language == 	other.language

 
    def __mul__(self,copies):
        'make clones of an animal'
        assert type(copies) == int and copies > 0, f'{copies} is not an int greater than 0'
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
        assert type(other) == Animal, f'You can only combine another anmial'
        return Animal(self.species+"/"+other.species, self.language+"/"+other.language)

class Bird(Animal):
    'a class that extends Animal for a bird'
    
    def fly(self, n):
        '''returns a message about the height of flight.
            Notice only birds, not animals can fly. '''
        assert type(n) == int and n > 0, f'{n} is not an int greater than 0'
        if self.sleeping==False:
            return 'I am flying {} feet!'.format(n)
        else:
            return 'I am sleeping! Leave me alone!'

    def __init__(self,lang='chirp'):
        'Bird constructor. Calls into the Animal constructor'
        #do I need an assert statement here?
        Animal.__init__(self,'bird',lang)

    def __repr__(self):
        'Bird representation'
        return "Bird('{}')".format(self.language)
