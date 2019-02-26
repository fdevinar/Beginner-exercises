'''The function should recognise if a subject line is stressful.
A stressful subject line means that all letters are in uppercase,
and/or ends by at least 3 exclamation marks, and/or contains at least
one of the following “red” words: "help", "asap", "urgent".
Any of those "red" words can be spelled in different ways -
"HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P",
even in a very loooong way "HHHEEEEEEEEELLP"

Input: Subject line as a string.
Output: Boolean.'''

def is_stressful(subject):

    import re

    if (subject[:-4:-1] == '!!!'):
        return True
    
    if subject.isupper():
        return True

    words = subject.split()
    for word in words:
        cleanword = re.sub('[^A-Za-z0-9]+','',word).upper()
        if cleanword in ('HELP', 'ASAP', 'URGENT'):
            return True
        else:
            finalword = ''
            for letter in cleanword:
                if letter not in finalword:
                    finalword = finalword + letter
            if finalword in ('HELP', 'ASP', 'URGENT'):
                return True
    return False
        
subject = input()

if len(subject)>100:
    print ('Subject is too long')
else:
    print(is_stressful(subject))



