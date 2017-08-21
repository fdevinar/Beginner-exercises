#Falta comentar o código abaixo
import getpass
import os
hidden_word = []
secret_word = []
wrong_letters = []
os.system('color 1f')
enter_secret_word = getpass.getpass('Enter the secret word: ')
print ('Pick the number of chances: ')
chances = input()
chances = int(chances)
#Generates hidden word
for idx,letter in enumerate(enter_secret_word):
    hidden_word.append("_")
    secret_word.append(letter)
print ('\n')
while chances > 0:
    os.system('cls')
    print ('Chances: ' + str(chances))
    print ('Wrong letters: ' + str(wrong_letters))
    print ('Hidden word: ' + str(hidden_word) + '\n')
    print ('Guess a letter: ')
    guess_letter = input()
    try:
        indices = [i for i, x in enumerate(secret_word) if x == guess_letter]
        for idx in indices:
            hidden_word[idx] = guess_letter
        if indices == []:
            raise Exception
        print ('You guessed right!')
        print ('--------------------------------------------')
        if hidden_word == secret_word:
            print ('Congratulations, you won the game!')
            print ('You guessed the word: ' + enter_secret_word)
            pause = input()
            quit()
    except Exception as err:
        print ('You guessed wrong! :(')
        chances = chances - 1
        wrong_letters.append(guess_letter)
        print ('You have ' + str(chances) + ' chances left')
        print ('\n')
        if chances == 0:
            print ('Sorry, you lost the game, keep trying!')
            pause = input()
            quit()
