import random

#Pick the range of integers to generate random numbers, and convert them to int
print ('Choose range of integers')
rng_int1 = input()
rng_int2 = input()
rng_int1 = int(rng_int1)
rng_int2 = int(rng_int2)

#Pick the number of integers to be generated, and initialize list
print ('Number of random integers generated:')
iterate = input()
iterate = int(iterate)
sorted_list = []

#Iterate and generate the random list
count = 0
while (count < iterate):
    sorted_list.append(random.randint(rng_int1,rng_int2))
    count = count + 1
    #print (sorted_list)

#Sort and each line of the list
sorted_list.sort()
for line in sorted_list:
    print (line)

print ('Bye!')
pause=input()
