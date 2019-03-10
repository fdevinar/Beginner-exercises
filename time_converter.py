def time_converter (time):
    print ('Tamanho: ' + str(len(time)))
    if (int(time[0:2:1]) >= 12):
        print ('PM')
    else:
        print ('AM')

    
    print (time[0:2:1])
    print (time[3:5:1])





time_converter('23:15')


