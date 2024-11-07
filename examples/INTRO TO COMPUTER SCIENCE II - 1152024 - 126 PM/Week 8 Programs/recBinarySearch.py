def recBinSearch(x, nums, low, high):
    if low > high:
        return -1
    mid = (low+high) // 2
    item = nums[mid]
    if x == item:
        return mid
    elif x < item:
        print("recBinSearch({}, {})".format(low, mid-1))
        # Search the left half
        return recBinSearch (x, nums, low, mid-1)
    else: # x > item
        print("recBinSearch({}, {})".format(mid+1, high))
        # Search the right half
        return recBinSearch (x, nums, mid+1, high)

def recBinarySearch (x, nums):
    low = 0
    high = len (nums) - 1
    print("recBinSearch({}, {})".format(low, high))
    return recBinSearch(x, nums, low, high)

