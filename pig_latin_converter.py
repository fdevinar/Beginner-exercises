#import sys

def pig_latin ():

    print ('My first function using Python, Pig Latin converter!')

    #Define loop condition ("Y" means this will enter the loop)
    type_new = 'Y'

    while (type_new == 'Y'):
        print ('Please type a word:')
        word = input()
        print ('This is your new word:')
    #Setting new word as 'second letter until the end' + 'first letter' + 'ay!'
        new_word = (word[1:] + word[0] + 'ay!')
    #While printing, make sure only first letter is upper-case
        print (new_word[0].upper() + new_word[1:].lower())
    #Setting loop condition different from 'Y'
        type_new = 'N'
        print('Type a new word?(Y/N)')
    #Asking if user wants to type a new word
        type_new = input()
    #Formatting to Upper-case to avoid confusion
        type_new = type_new.upper()
    print('Thank you for playing!')    

pig_latin()

