# Didn't collaborate with anyone on this assignment


class Person(object):
    '''A class representing a person that takes in 3 parameters'''
    def __init__(self, name, age, email = ''):
        'The constructor which sets variables based on parameters and asserts type'
        assert type(name) == str, 'name is not a string'
        assert len(name) >0, 'Name must be a string with a length greater than 0'
        assert int(age), 'age is an integer'
        assert age > 0, 'age must be greater than 0'
        assert type(email) == str, 'Email must be a string'
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        'The string for repr Person'
        return f'Person {self.name} is {self.age} years old. Their email address is {self.email}'
    
    def __repr__(self):
        'The representation of the Person class'
        return f'Person({self.name},{self.age},{self.email})'
    
    def setName(self, name):
        'A method that will set the name of the Person class'
        assert type(name) == str and len(name) > 0, 'name must be a string and have a length greater than 0'
        self.name = name
        return self.name
    
    def setAge(self, age):
        'Age setting method'
        assert int(age) and age>0, 'Age must be an integer and greater than 0'
        self.age = age
        return self.age
    
    def setEmail(self, email):
        'Email setting method'
        assert str(email), 'Email must be a string'
        self.email = email
        return self.email
    
    def getName(self):
        'returns the name variable'
        return self.name
    
    def getAge(self):
        'returns age variable'
        return self.age

    def getEmail(self):
        'returns email variable'
        return self.email
        

class Student(Person):
    'A class representing a student'
    def __init__(self, name, age, email, year):
        'the constructor for the student class'
        assert type(name) == str, 'name is not a string'
        assert len(name) >0, 'Name must be a string with a length greater than 0'
        assert int(age), 'age is an integer'
        assert age > 0, 'age must be greater than 0'
        assert type(email) == str, 'Email must be a string'
        assert len(email) > 5, 'Email must have more than 5 characters'
        assert year == 'Sophmore' or year == 'Freshman' or year == 'Junior' or year == 'Senior' and str(year), 'year must be a string and value of Freshman, Sophmore, Junior, or Senior'
        self.name = name
        self.age = age
        self.email = email
        self.year = year

    def setYearInProgram(self, year):
        'Method that sets the year of the student'
        assert year == 'Sophmore' or year == 'Freshman' or year == 'Junior' or year == 'Senior' and str(year), 'year must be a string and value of Freshman, Sophmore, Junior, or Senior'
        self.year = year

    def getYearInProgram(self):
        'Method that returns year'
        return self.year
    
    def __repr__(self):
        'representation of the student class'
        return f'Student({self.name},{self.age},{self.email},{self.year})'
    
    def __str__(self):
        'The string for repr student'
        return f'Student {self.name} is {self.age} years old. Their email address is {self.email} and they are a {self.year}'
    

class Instructor(Person):
    'Instructor class building on the person class'
    def __init__(self, name, age, email, office):
        'constructor for the Instructor class'
        assert type(name) == str, 'name is not a string'
        assert len(name) >0, 'Name must be a string with a length greater than 0'
        assert int(age), 'age is an integer'
        assert age > 0, 'age must be greater than 0'
        assert type(email) == str, 'Email must be a string'
        assert len(email) > 5, 'Email must have more than 5 characters'
        assert str(office) and len(office) > 0, 'Office must be a string with length greater than 0' 
        self.name = name
        self.age = age
        self.email = email
        self.office = office

    def setOffice(self, office):
        'set office method'
        assert str(office) and len(office) > 0, 'Office must be a string with length greater than 0' 
        self.office = office

    def getOffice(self):
        'returns office'
        return self.office
    
    def __repr__(self):
        'repr for the instructor class'
        return f'Instructor({self.name},{self.name},{self.email},{self.office})'

    def __str__(self):
        'The string for repr student'
        return f'Instructor {self.name} is {self.age} years old. Their email address is {self.email} and they located in office {self.office}'
    
class Professor(Instructor):
    'A class building on instructor including a research area parameter'
    def __init__(self, name, age, email, office, researchArea):
        assert type(name) == str, 'name is not a string'
        assert len(name) >0, 'Name must be a string with a length greater than 0'
        assert int(age), 'age is an integer'
        assert age > 0, 'age must be greater than 0'
        assert type(email) == str, 'Email must be a string'
        assert len(email) > 5, 'Email must have more than 5 characters'
        assert str(office) and len(office) > 0, 'Office must be a string with length greater than 0' 
        assert str(researchArea) and len(researchArea) > 0, 'researchArea must be a string and longer than 0 chars'
        self.name = name
        self.age = age
        self.email = email
        self.office = office
        self.researchArea = researchArea

    def __repr__(self):
        'repr of Professor class'
        return f'Professor({self.name},{self.name},{self.email},{self.office},{self.researchArea})'
    

    def __str__(self):
        'The string for repr Professor'
        return f'Instructor {self.name} is {self.age} years old. Their email address is {self.email} and they are located in office {self.office}. Their research area is {self.researchArea}'

    def getResearchArea(self):
        'returns research area'
        return self.researchArea
    

