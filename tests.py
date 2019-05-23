# https://py.checkio.org/en/mission/between-markers/

def between_markers (string, init, final):
    first = string.find(init)
    last = string.find(final)

    print ('First:', first, ' Last:' , last)

    if (first == -1 and last == -1):
        print ('Loop 1')
        return (string)

    if (first == -1):
        print ('Loop 2')
        return (string[0:last])

    if (last == -1):
        print ('Loop 3')
        return (string[first+len(init):999])

    if (last < first):
        print ('Loop 4')
        return ''

    print ('Loop 5')
    return (string[(first+len(init)):last])    


#print (between_markers('What is >apple<', '>', '<'))
#print(between_markers('No[/b] hi', '[b]', '[/b]'))

#print(between_markers("<head><title>My new site</title></head>","<title>","</title>"))

print(between_markers("No [b]hi","[b]","[/b]"))
