''' Convert LBS to KG '''

print ('Number of conversions:')
number = input()
number = int(number)
convlist = []

while (number > 0):
    print ('Conversion value #' + str(number) + ' (Lbs):')
    convlist.append(input())
    number -= 1

print ('Results:')

for value in convlist:
    print (value + ' Lbs = ' + str((float(value)*0.453592)) + ' Kg')

input()
