def threeNumberSum(array, targetSum):
    array.sort()
    newarr = []

    for i in range(len(array)-2):
        left = i + 1
        right = len(array)-1
        print('this bit works')

        while left < right:        
            cs = array[i] + array[left] + array[right]

            if cs == targetSum:
                newarr.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif cs < targetSum:
                left += 1
            else:
                right -= 1
                

                
    return newarr



# x= [12, 3, 1, 2, -6, 5, -8, 6]
# y =0

# print(threeNumberSum(x,y))