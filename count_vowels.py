print ('Type a word: ')
word = input()
vowels = ('a','e','i','o','u')
vowlist = []

for letter in word:
    if letter in vowels:
        vowlist.append(letter)

a = []
e = []
i = []
o = []
u = []

for letter in vowlist:
    if letter == 'a':
        a.append(letter)
    elif letter == 'e':
        e.append(letter)
    elif letter == 'i':
        i.append(letter)
    elif letter == 'o':
        o.append(letter)
    else:
        u.append(letter)
        
print ('Your word has ' + str(len(a)) + ' letter(s) A, ' + str(len(e)) + \
       ' letter(s) E, ' + str(len(i)) + ' letter(s) I, ' + str(len(o)) + \
       ' letter(s) O, and ' + str(len(u)) + ' letter(s) U.' )

pause=input()
