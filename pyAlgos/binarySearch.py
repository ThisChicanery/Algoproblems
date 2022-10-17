import math

def binarySearch(array, target):
    array.sort()
    left = 0
    right = len(array) -1
    
    while left <= right:
        m = math.floor((left+right)/2)
        if array[m] == target:
            return m
        elif array[m] > target:
            right = m - 1
        else:
            left  = m + 1
    
    return -1
        

x = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
y = 33

print(binarySearch(x,y))