#Falta comentar o código abaixo
import getpass
import os
#Initializes hidden word (with "_"), secret word list and wrong letters list
hidden_word = []
secret_word = []
wrong_letters = []
#Blue background, bright white font
os.system('color 1f')
#Getpass used to hide the word being typed
enter_secret_word = getpass.getpass('Enter the secret word: ')
print ('Pick the number of chances: ')
chances = input()
chances = int(chances)
#At first it fills hidden_word list with "_"
#Afterwards, it fills with the appropriate letter if guessed correctly
for idx,letter in enumerate(enter_secret_word):
    hidden_word.append("_")
    secret_word.append(letter)
print ('\n')
#Loops while user has chances left
while chances > 0:
    #Cleans the screen
    os.system('cls')
    #Prints chances, letters guessed incorrectly and hidden word
    print ('Chances: ' + str(chances))
    print ('Wrong letters: ' + str(wrong_letters))
    print ('Hidden word: ' + str(hidden_word) + '\n')
    print ('Guess a letter: ')
    guess_letter = input()
    try:
        #If the guessed letter has more than 1 place on list,
        #iterates to get the indices
        indices = [i for i, x in enumerate(secret_word) if x == guess_letter]
        #Fills the list according to index got on previous step
        for idx in indices:
            hidden_word[idx] = guess_letter
        #If letter was guessed incorrectly, forces an exception
        # to "you guessed wrong" step
        if indices == []:
            raise Exception
        print ('You guessed right!')
        print ('--------------------------------------------')
        #User wins if the hidden (_) gets filled completely
        if hidden_word == secret_word:
            print ('Congratulations, you won the game!')
            print ('You guessed the word: ' + enter_secret_word)
            #Pauses so user can see "victory" screen, then leaves game.
            pause = input()
            quit()
    except Exception as err:
        print ('You guessed wrong! :(')
        chances = chances - 1
        #Incorrect guesses adds to list displayed after Try: command
        wrong_letters.append(guess_letter)
        print ('You have ' + str(chances) + ' chances left')
        print ('\n')
        #User loses if it has no more chances,
        # pauses the game to display "losing" screen.
        if chances == 0:
            print ('Sorry, you lost the game, keep trying!')
            pause = input()
            quit()
