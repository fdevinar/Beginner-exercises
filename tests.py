# https://py.checkio.org/en/mission/popular-words/

def popular_words (text, array):

    text = text.lower()
    text = text.split()

    print (text)
    
    popudict = {}

    for word in array:
        if word in text:
            if (word in popudict.keys()):
                popudict.update({word: (popudict.get(word)+1)})
            else:
                popudict.update({word: 1})
        else:
            popudict.update({word: 0})
            
    return (popudict)    

#logica incorreta - nao deveria loopar por array
print (popular_words('a b c',['a','b','b','b','c','d']))

print (popular_words('When I was One I had just begun When I was Two I was nearly new',['i','was','three','near']))

