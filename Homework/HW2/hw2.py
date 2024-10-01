
#Question 1:
class Engine(object):
    'a class that represents an Engine'

    def __init__(self, name,maxSpeed=0, state='off'):
        'constructor to initialize an Engine'
        self.name = name
        self.state = state
        assert maxSpeed >= 0, f'Max speed is negative'
        self.maxSpeed = maxSpeed
        
        self.speed = 0
        self.state = state

    
    def setEngine(self, name):
        'Set the type of engine'
        self.name = name

    def increaseSpeed(self, speed):
        'increase the speed of the engine'
        assert int(speed), 'Speed is not an integer'
        assert speed > 0, 'Speed must be greater than 0'
        
        if self.state == 'on':
            if self.speed + speed >= self.maxSpeed:
                return "That's too fast! input a smaller number."
            else:
                self.speed += speed
                return self.speed
        else:
            return f'Engine is off, please turn on to change speed'

    def decreaseSpeed(self, speed):    
        'decreases the speed of the engine'
        assert int(speed), 'Speed is not an integer'
        assert speed > 0, 'Speed must be greater than 0.'

    def turnOn(self):
        'turns on the engine to a specifed speed'
        if self.state == 'off':
            self.state = 'on'
            return 'Engine turned on'
        elif self.state == 'on':
            return 'Engine is on'
        else:
            return 'state is outside specificed on/off'
    
    def turnOff(self):
        if self.state == 'on':
            if self.speed != 0:
                return 'Speed must be 0 to turn off!'
            elif self.speed == 0:
                self.state = 'off'
                return 'Engine turned off'



    def getName(self):
        'returns the name of the engine'
        return self.name

    def getMaxSpeed(self):
        'returns the max speed of the engine'
        return self.maxSpeed
        

    def getSpeed(self):
        'returns the current speed of the engine'
        return self.speed
    
    def getState(self):
        'returns the state of the engine'
        return self.state


    def __str__(self):
        'The string representation of an Engine'
        return f'{self.name},{self.maxSpeed},{self.state}' 
    
    def __repr__(self):
        'The representation of an Engine'
        return f'Engine({self.name},{self.speed},{self.state})'

        

        
    
    
    # YOU MUST WRITE THE REST OF THE METHODS YOURSELF. NOT PROVIDED
    

#QUESTIONS 2 add 3:
#saving and initializing types to/from file

def saveEngineInfo(filename, engines):
    'save engine to a file'
    try:
        outfile = open(f'{filename}.txt', 'w')
        for engine in engines:
            outfile.write(f'{engine.getName()}, {engine.getMaxSpeed()}, {engine.getState()}\n')
        outfile.close()
    except Exception as e:
        print(e)


def loadEngines(filename):
    'load engines from a file'
    try:
        engines=[]
        infile = open(f'{filename}.txt', 'r')
        data_lines = infile.readlines()
        for line in data_lines:
            engine_data = line.strip().split(',')
            e = Engine(engine_data[0],int(engine_data[1]),engine_data[2].strip())
            engines.append(e)
        return engines
    except Exception as e:
        print(e)

