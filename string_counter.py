from operator import itemgetter 
with open('text.txt') as f:
    data = f.readlines()

cleanstring = []

#Creates a string list from text file 'text.txt'
for each_word in data:
    stringlist = each_word.split(' ')

#Cleans the list
for word in stringlist:
    word = word.translate({ord(c): None for c in '\'!@#$:.,?'})
    cleanstring.append(word)

wordcount={}

for word in cleanstring:
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

#print (wordcount)

sortedword = sorted(wordcount.items(), key=itemgetter(1),reverse=True)

print (sortedword)


