#lab 1
def longestWord(filename):
    '''reads a file to a variable,
    then removes the symbols other that english letters
    splits the str into a list with each object a word
    adds the word to a dictionary as a value with the key being 
    the amount of characters in each str object'''
    file = open(filename, 'r')
    content = file.read()
    x= '?,.!;:'
    y = '      '
    mytable = str.maketrans(x,y)
    transContent = content.translate(mytable)
    wordList = transContent.split()
    lenDict = {}
    max_key = 0
    for word in wordList:
        lenDict.update({len(word):word})
    try:    
        return print(f'The longest word contains : {max(lenDict.keys())} characters')
    except ValueError:
        print('Contains no objects')

def uniqueWordCount(filename):
    '''Reads file to variable,
    translates to lower and not special characters
    splits str into lst
    if the word isnt in the dictionary, it is added with a value of one.
    if it is contained in the dict, the value is incremented by one
    returns dict'''
    file = open(filename, 'r')
    content = file.read()
    x= '?,.!;:'
    y = '      '
    mytable = str.maketrans(x,y)
    transContent = content.translate(mytable)
    wordList = transContent.split() 
    countDict = {}
    try:
        for word in wordList:
            lowWord = word.lower()
            if lowWord not in countDict:
                countDict.update({lowWord:1}) 
            else: 
                
                countDict[lowWord] += 1
    except ValueError:
        print('Empty dictionary')
    except UnboundLocalError:
        print('{}')
                
    return countDict


print(longestWord('sampleFile1.txt'))
print(longestWord('sampleFile2.txt'))
print(longestWord('sampleFile3.txt'))

print(uniqueWordCount('sampleFile1.txt'))
print(uniqueWordCount('sampleFile2.txt'))
print(uniqueWordCount('sampleFile3.txt'))


