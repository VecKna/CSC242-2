def errorf():
    try:
        f = open('mfile2.txt')
        s = f.readline()
        f.close()
        i = int(s)
        print(s)
        raise Exception("I just wanted to cause trouble.")
    except (IOError, FileNotFoundError) as e:
        print("I/O error: {}".format(e))
    except ValueError as err:
        print("Could not convert data to an integer: {}".format(err))
    except Exception as err:
        print("Unexpected error: {}".format(err))
        raise

errorf()


