# Brute Force attempt
def twoNumberSum(array, targetSum):
    for i in array:
        for j in array:
            if i != j and i + j == targetSum:
                return [i,j]

    return []

# O(N)^2 time, O(N) space


def twoNumberSum2(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum > targetSum:
            right -= 1 
        else:
            left += 1


    return ["Empty"]

# 0(N)log(n) time because of the sorting algorithm, O(N) space

def twoNumberSum3(array, targetSum):
    newdict = {}
    for i in array:
        valueNeeded = targetSum - i
        if valueNeeded in newdict:
            return [i, valueNeeded]
        else:
            newdict[i] = i


    return ['empty']


# O(N) time, 0(N) Space



# x = [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47]
# y = 163

# print(twoNumberSum3(x,y))


