def check_palindrome ():
    word_list = []
    print('Please type a word, the system will check if it\'s a palindrome.')
    word = input()
    #Creates a list based on word typed.
    for letter in word:
        word_list.append(letter)
    #Check is list is equal to list reversed.
    if word_list == word_list[::-1]:
        print ('Word: ' + word + ' IS a Palindrome!\n')
        print ('Type Y to check a new word.')
        choice = input()
        #Accepts 'Y' or 'y' as positive answer.
        choice = choice.upper()
        return choice
    else:
        print ('Word: ' + word + ' is NOT a Palindrome!\n')
        print ('Type Y to check a new word.')
        choice = input()
        choice = choice.upper()
        return choice

choice = 'Y'
while choice == 'Y':
    choice = check_palindrome()
print ('Thank you for playing!')


