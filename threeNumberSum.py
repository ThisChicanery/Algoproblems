def threeNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array)-1
    newarr = []
    for i in array:
 
        currentSum = i + array[left] + array[right]

        while left < right:
            if currentSum == targetSum:
                newarr.append([i,array[left],array[right]])
            elif currentSum > targetSum:
                right -= 1
            else:
                left += 1
            
            
        

    return newarr
