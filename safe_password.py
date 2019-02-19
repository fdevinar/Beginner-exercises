#Checks if a password has
# A) at least 10 characters
# B) upper case letter
# C) lower case letter
# D) a digit(number)

print('Please type a password:')
word = input()
print('Checking security......')


def checksafe(word):
    if len(word)<10:
        return 'No'
    upper=0
    lower=0
    digit=0
    for letter in word:
        if letter.isupper():
            upper=1
        if letter.islower():
            lower=1
        if letter.isdigit():
            digit=1
    #print (upper,lower,digit)
    if (upper and lower and digit):
        return 'Yes'
    return 'No'
    
print('Is the password secure?')

print(checksafe(word))

