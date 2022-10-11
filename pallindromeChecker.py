def isPalindrome(string):
    counter = len(string) -1
    for i in string:
        if i == string[counter]:
            counter -=1
        else:
            break
    
    return counter == -1


x = 'abcdefghihgfedcba'
y = 'abcdefghihgfeddcba'
print(isPalindrome(x))