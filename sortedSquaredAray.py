# def sortedSquaredArray(array):
#     newarr = []

#     for i in array:

#         newarr.append(i*i)

#     newarr.sort()
#     return newarr

# # 0(nlog(n)) time, 0(n) space





# 0(n) time  and 0(n) space

def sortedSquaredArray2(array):

    newArray = [0 for _ in array]
    smallValueIndex= 0
    largeValueIndex = len(array) -1 

    for i in reversed(range(len(array))):
        smallValue = array[smallValueIndex]
        largeValue = array[largeValueIndex]


        if abs(smallValue) > abs(largeValue):
            newArray[i] = smallValue * smallValue
            smallValueIndex +=1
        else:
            newArray[i] = largeValue * largeValue
            largeValueIndex -= 1


    return newArray



# x= [1, 2, 3, 5, 6, 8, 9]
# print(sortedSquaredArray2(X))



