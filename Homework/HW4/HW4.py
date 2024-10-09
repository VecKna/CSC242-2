'''
CSC 242 Homework 4
Collaborators: NONE
'''

class Book(object):
    'Book class'
    def __init__(self, name, author, pages = 1, year = 1440):
        'Constructor for thew book class'
        assert type(name) == str and len(name) >= 1,'name must be a string and have a length greater than 0'
        assert type(author) == str and len(author) >= 1,'author must be a string and have a length greater than 0'
        assert type(pages) == int and pages >= 1, 'pages must be an integer and have one or more pages'
        assert type(year) == int and year >= 1440, 'year must be an integer with a value equal or greater to 1440'
        self.name = name
        self.author = author
        self.pages = pages
        self.year = year

    def getName(self): 
        return self.name

    def getAuthor(self):
        return self.author

    def getYear(self):
        return self.year

    def getPages(self):
        return self.pages

    def __str__(self):
        return f'{self.name}:{self.author}:{self.pages}:{self.year}'

    def __repr__(self):
        return f'Book({self.name},{self.author},{self.pages},{self.year})'
    
    def __add__(self, other):
        return Book()
    

class Library(Book):
    'Library collection of book objects'
    def __init__(self, filename = 'filename.txt'):
        self.library = []
        self.filename = filename

    def addBook(self, book):
        'adds a book to the library'
        assert isinstance(book, Book), 'Can only add books to the library'
        self.library.append(book)


    def getBooksWithAuthor(self, author):
        assert type(author) == str and len(author) >= 1,'author must be a string and have length greater than 0'
        result = []
        for items in self.library:
            if items.getAuthor() == author:
                result.append(str(items))
            else:
                result.append(None)
        return result

    def getBooksWrittenInYear(self, year):
        assert type(year) == int, 'year must be an integer'
        result = []
        for items in self.library:
            if items.getYear() == year:
                result.append(repr(items))
            else:
                result.append(None)
        return result
            

    def getBookswithPageCountRange(self, min, max):
        assert type(min) == int and min > 0, 'must be an integer and greater than 0'
        assert type(max) == int, 'must be an integer'
        result = []
        for items in self.library:
            if items.getPages() >= min and items.getPages() <= max:
                result.append(repr(items))
            else:
                result.append(None)
        return result

    def getBooksWithNameContaining(self, letter):
        assert type(letter) == str and len(letter) > 0, 'Must be a str and len > 0'
        result = []
        for items in self.library:
            if letter in items.getName():
                result.append(repr(items))
        return result
    
#Problem 3

    def __len__(self):
        'len'
        return len(self.library)
    
    def __iter__(self):
        'iterator'
        return iter(self.library)
    
    def __getitem__(self, index):
        'indexer'
        assert type(index) == int, 'index must be an int'
        return self.library[index]
    
#problem 4

    def writeBooksToFile(self):
        'write books to file'
        try:
            outfile = open(self.filename, 'w')
            for book in self.library:
                outfile.write(f'{book}\n')
            outfile.close()
            return True
        except Exception as e:
            print(e)
            return False

    def loadBooks(self):
        'load books from file'
        try:
            infile = open(self.filename, 'r')
            self.library.clear()
            lines = infile.readlines()
            for line in lines:
                book_data = line.strip().split(':')
                self.library.append(Book(book_data[0],book_data[1],int(book_data[2]),int(book_data[3])))
            return True
        except Exception as e:
            print(e)
            return False



        

