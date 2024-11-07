def recBinSearch(x, nums, low, high):
    pass
            
def recBinarySearch (x, nums):
    low = 0
    high = len (nums) - 1
    print("recBinSearch({}, {})".format(low, high))
    return recBinSearch(x, nums, low, high)
