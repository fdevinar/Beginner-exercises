'''
You are given a text, which contains different english letters and
punctuation symbols. You should find the most frequent letter in the
text.
The letter returned must be in lower case. While checking for the most
wanted letter, casing does not matter, so for the purpose of your
search, "A" == "a". Make sure you do not count punctuation symbols,
digits and whitespaces, only letters.

If you have two or more letters with the same frequency, then return
the letter which comes first in the latin alphabet. For example --
"one" contains "o", "n", "e" only once for each, thus we choose "e".

Input: A text for analysis as a string.

Output: The most frequent letter in lower case as a string.
'''

import re, operator

word = '12345,12345,12345 S 12345,12345'#input()
word = word.lower()
#Pay attention to spaces after commas on re.sub
#Removes numbers
word = ''.join([i for i in word if not i.isdigit()])
#Removes spaces and symbols
word = re.sub('\W+', '', word)

print(word)

'''
wdict = {}
for letter in word:
    if letter in wdict:
        wdict[letter] += 1
    else:
        wdict[letter] = 1

print ('Dicionario:')
print (wdict)

highnumber = 0

for number in wdict:
    if wdict[number] > highnumber:
        highnumber = wdict[number]

print ('Numero mais alto:')
print (highnumber)

listdict = (wdict.items())
print (listdict)

ordlist = sorted(listdict, key=lambda x:(-x[1],x[0]))

print(ordlist)

mostwanted = ordlist[0]
print('Most wanted letter:')
print (mostwanted[0])
'''

