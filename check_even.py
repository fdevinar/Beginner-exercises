num = input()
list(num)
even = 0
uneven = 0

for n in num:
    if (int(n)%2 != 1):
        print ('Par/Even')
        even += 1
    else:
        print ('Impar/Uneven')
        uneven += 1

print ('Even: ' + str(even) + ' - Uneven: ' + str(uneven))
