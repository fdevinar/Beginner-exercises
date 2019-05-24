#(a) 3+4+5+6+7+8+9, (b) 9+10+11+12, (c) 13+14+15 and (d) 42.

consecutive = 0
num = 42
count = 0
numlist = []
soma = 0

for x in range(1, num+1):
    numlist.append(x)

print (numlist)

#print(sum(numlist))

'''
print (sum(numlist[count:count]))
print (sum(numlist[count:count+1]))
print (sum(numlist[count:count+2]))
print (sum(numlist[count:count+3]))
print (sum(numlist[count:count+4]))
'''


x = 0


while (soma < num):
    print ('**********************')
    print ('Count:')
    print (count)
    print ('Soma:')
    print (sum(numlist[x:count]))
    print (numlist[x:count])
    soma = (sum(numlist[x:count]))
    if (soma == num):
        consecutive += 1
    print('Nova soma:')
    print (soma)
    count += 1

#print ('Resultado final:')
#print (consecutive)

'''


print (numlist[0:0])
print (sum((numlist[0:0]))) = 0

print (numlist[0:1])
print (sum((numlist[0:1]))) = 1


print (numlist[0:2])
print (sum((numlist[0:2]))) = 3


print (numlist[0:3])
print (sum((numlist[0:3]))) = 6

print (numlist[0:4])
print (sum((numlist[0:4]))) = 10

print (numlist[0:5])
print (sum((numlist[0:5]))) = 15
'''

'''
print ('Next loop')

print (numlist[0+1:0+1])
print (sum((numlist[0+1:0+1])))

print (numlist[0+1:1+1])
print (sum((numlist[0+1:1+1])))


print (numlist[0+1:2+1])
print (sum((numlist[0+1:2+1])))


print (numlist[0+1:3+1])
print (sum((numlist[0+1:3+1])))

print (numlist[0+1:4+1])
print (sum((numlist[0+1:4+1])))

print (numlist[0+1:5+1])
print (sum((numlist[0+1:5+1])))

print ('Next loop')
'''









