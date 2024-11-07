import os

rules={'Virus1':'iyfp9fg394g539gf',
       'Virus2':'9f8g8408h3498hff'}

def scan(pathname, signatures):
    print('IM IN FOLDER:' , pathname)
    '''recursively scans all files contained, directly or
       indirectly, in the folder pathname'''
    for item in os.listdir(pathname):       # for every file or
                                            # folder in folder
                                            # pathname 
        # join folder pathname and item name
        # next = pathname + '/' + item	    # Mac only
        # next = pathname + '\' + item	    # Windows only
        n = os.path.join(pathname, item) # any OS
        if os.path.isdir(n):
            scan(n, signatures)
        else: # n is a file
            f = open(n, 'r')
            s = f.read()
            for virus in signatures:
                if s.find(signatures[virus]) > 0:
                    print('{}, found virus {}'.format(n,virus))
            f.close()

scan('test', rules)
#scan('test\\test1',rules)
