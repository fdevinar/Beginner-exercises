#https://py.checkio.org/en/mission/non-unique-elements/

def checkio(array):
    non_unique_list = []
    for element in array:
        if (array.count(element) > 1):
            non_unique_list.append(element)

    return (non_unique_list)
            


#checkio(['1','2','1','2','3'])

print (checkio(['5','5','5','5','5']))

