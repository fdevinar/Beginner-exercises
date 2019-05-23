# https://py.checkio.org/en/mission/popular-words/

def popular_words (text, array):

    text = text.lower()
    text = text.split()

    print (text)
    
    popudict = {}

    for word in array:
        if word in text:
            print (word)
            popudict.update({word: (text.count(word))})
        else:
            popudict.update({word: 0})

    return (popudict)
        
print (popular_words('When I was One I had just begun When I was Two I was nearly new',['i','was','three','near']))

