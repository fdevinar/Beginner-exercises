'''
all_the_same([1, 1, 1]) == True

all_the_same([1, 2, 1]) == False

all_the_same(['a', 'a', 'a']) == True

all_the_same([]) == True
'''

def all_the_same (lista):
    if not lista:
        return True

    comp = lista[0]
    equal = False


    
    for element in lista:
        if (element == comp):
            equal = True
        else:
            return False
    if (equal):
        return True


print (all_the_same([]))
        
        
