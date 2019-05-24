''' Positive integers can be expressed as sums of consecutive positive integers in various ways.
For example, 42 can be expressed as such a sum in four different ways:
'''
#(a) 3+4+5+6+7+8+9, (b) 9+10+11+12, (c) 13+14+15 and (d) 42.
'''
As the last solution (d) shows, any positive integer can always be trivially expressed
as a singleton sum that consists of that integer alone.

Compute how many different ways it can be expressed as a sum of consecutive positive integers.

count_consecutive_summers(42) == 4

count_consecutive_summers(99) == 6
'''

num = 42
count = 0


def consecutive (count):
    count += 1
    print (count)
    if (count <= num):
        consecutive(count)


consecutive(0)


'''
while (count <= num):
    print (count, ' ' ,num)
    count += 1
    sum += 1
    #print (sum)
'''
