def iterBinarySearch(x, nums):
    'look for x in a sorted list nums'
    low = 0
    high = len (nums) - 1
    while low <= high:
        mid = (low+high) // 2
        item = nums[mid]
        if x == item:
            return mid
        elif x < item:
            # Item is in the left part of the list
            high = mid - 1
        else:
            # Item is in the right part of the list
            low = mid + 1
    return -1
