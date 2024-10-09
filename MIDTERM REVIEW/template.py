import random

class Magic8Ball(object):

    def __init__(self, answers=[]):
        'the constructor'
        assert type(answers)==list, 'Must provide a list'
        if len(answers)==0:
            answers.append('It is certain')
            answers.append('It is decidedly so')
            answers.append('Without a doubt')
            answers.append('Yes definitely')
            answers.append('You may rely on it')
            answers.append('As I see it, yes')
            answers.append('Most likely')
            answers.append('Outlook good')
            answers.append('Yes')
            answers.append('Signs point to yes')
            answers.append('Reply hazy try again')
            answers.append('Ask again later')
            answers.append('Better not tell you now')
            answers.append('Cannot predict now')
            answers.append('Concentrate and ask again')
            answers.append("Don't count on it")
            answers.append('My reply is no')
            answers.append('My sources say no')
            answers.append('Outlook not so good')
            answers.append('Very doubtful')
            self.__answers = answers


    def shake(self):
        'get the next answer'
        v = random.randrange(0, len(self.__answers))
        self.__current = self.__answers[v]


    def get(self):
        'get the current answer'
        return self.__current

    def numAnswers(self):
        'get the number of answers in the ball'
        return len(self.__answers)

    def __iter__(self):
        'get the iterator'
        return iter(self.__answers)

    def __str__(self):
        'string representation'
        return f'I am a Magic 8Ball with {self.numAnswers()} answers'



import random
class Cookie(object):

    #built in cookies, other cookies are allowed
    cookieTypes=('chocolate chip','peanut butter','oatmeal','mint chocolate','raisin','vegan')
    
    def __init__(self,cookieType=None):
        'constructor. Assigns a cookie name or randomly picks one from the built in cookie types'
        if cookieType==None:
            self.__cookie = self.cookieTypes[random.randint(0,len(self.cookieTypes)-1)]
        else:
            self.__cookie = cookieType

    def getCookieType(self):
        'return the cookie type'
        return self.__cookie

    def __str__(self):
        'string representation of cookie'
        return self.__cookie

    def __repr__(self):
        'pythin representation of cookie'
        return "Cookie('{}')".format(self.__cookie)

class CookieJar(object):
    pass
