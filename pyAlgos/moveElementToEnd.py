def moveElementToEnd(array, toMove):
    new = []
    new2 = []
    for i in array:
        if i == toMove:
            new.append(i)
        else:
            new2.append(i)
            
    for i in new:
        new2.append(i)
    
    return new2


#This algorithm is running in 0(n) time because the first loop is based on the length of the array
#The second for loop is iterating through the lenght of the moved values so it will also be a smaller 0(n)
#Adding the two makes this an 2 0(n) therefore making it 0(n)

#The sace complecixty is also 2 0(n) so 0(n)