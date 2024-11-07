import os

rules={'Virus1':'iyfp9fg394g539gf',
       'Virus2':'9f8g8408h3498hff'}

def scan(pathname, signatures):
    '''recursively scans all files contained, directly or
       indirectly, in the folder pathname'''
    for item in os.listdir(pathname):
        if item[0] != '.':
            n = os.path.join(pathname, item) # any OS
            try:
                scan(n, signatures)
            except: # base case: exception means that item is a file
                f = open(n, 'r')
                s = f.read()
                for virus in signatures:
                    if s.find(signatures[virus]) > 0:
                        print('{}, found virus {}'.format(n,virus))
                f.close()

#scan('test', rules)
#scan('test\\test1',rules)
