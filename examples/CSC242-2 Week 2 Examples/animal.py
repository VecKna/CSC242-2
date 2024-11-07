class Animal(object):
    'a class that abstracts an animal'
    def __init__(self, s = 'default', l = 'default'):
        self.species = s
        self.language = l
        
    def setSpecies(self, name):
        'sets the species of the animal'
        self.species = name
        
    def setLanguage(self, lang):
        'sets the language of the animal'
        self.language = lang
        
    def speak(self):
        return 'I am a {} and I {}'.format(self.species, self.language)
    
    def __repr__(self):
        return 'Animal({}, {})'.format(self.species, self.language)

    def __str__(self):
        return f'{self.species},{self.language}'

    def __add__(self, other):
        'create a hybrid animal'
        return Animal(self.species+"/"+other.species, self.language+"/"+other.language)

class Bird(Animal):
    'a class that extends Animal for a bird'
    
    def fly(self, n):
        'returns a message about the height of flight'
        return 'I am flying {} feet!'.format(n)
    
    def __init__(self, lang = 'chirp'):
        Animal.__init__(self, 'bird', lang)

    def __repr__(self):
        return "Bird({})".format(self.language)

    def __str__(self):
        return Animal.speak(self)
        

def loadAnimal(filename):
    try:
        infile=open(filename, 'w')
        lines = infile.readlines()
        for line in lines:
            data = line.strip().split()
        
        infile.close()
    except Exception as e:
        print(e) 
def writeToFile(filename, l):
    try:
        outfile=open(filename, 'w')
        for animal in l:
            outfile.write(str(animal+'\n'))
        outfile.close()
    except Exception as e:
        print(e) 
