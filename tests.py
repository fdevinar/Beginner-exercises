# https://py.checkio.org/en/mission/popular-words/

def popular_words (text, array):
    arrtext = text.split()

    popudict = {}

    for word in arrtext:
        if word in array:
            if word in popudict.keys():
                
                print ('Loopou')
                
            popudict.update({word: 1})

    print (popudict.keys())
    print (popudict.values())




popular_words('a b c',['a','b','b'])
