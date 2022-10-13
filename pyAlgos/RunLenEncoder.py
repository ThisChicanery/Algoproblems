def runLengthEncoding(string):
    newstr = ""
    counter = 1

    for i in range(len(string)):
        if i > len(string)-2:
            newstr += str(counter) + string[i]
            break
        else:
            if counter >= 9 and string[i] == string[i+1]:
                newstr += str(counter) +string[i]
                counter = 0
            if string[i] == string[i+1]:
                counter += 1
            else:
                newstr += str(counter) + string[i]
                counter = 1
        
        
    return newstr


x = 'AAAAAAAAAAAAABBCCCCDD'
answer = '9A4A2B4C2D'

print(runLengthEncoding(x))

