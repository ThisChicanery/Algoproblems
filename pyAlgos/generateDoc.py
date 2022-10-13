def generateDocument(characters, document):
    d = {}
    for i in characters:
        d[i] = d.get(i, 0) + 1


    for j in document:
        d[j] = d.get(j, 0) - 1
        if d[j] <= -1:
            return False
    
        
    return True

#My solution I think this is 2 for loops so O(n + M) and the space is O(n)

# x = "helloworldO"
# y = "hello wOrld"

# print(generateDocument(x,y))