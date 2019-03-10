def time_converter (time):

    if (len(time) == 5):
        hour = time[0:2:1]
        minute = time[3:5:1]
    else:
        hour = time[0:1:1]
        minute = time[2:4:1]

    if (int(hour) == 0 and int(minute) == 0):
        return ('12:00 a.m.')  

    if (int(hour[0:1:1]) == 0):
        hour = hour[1:2:1]

    if (int(hour) == 12):
        return (str(hour) + ':' + str(minute) + ' p.m.')
        
    if (int(hour) > 12):
        hour = int(hour) - 12
        return (str(hour) + ':' + str(minute) + ' p.m.')
    else:
        return (str(hour) + ':' + str(minute) + ' a.m.')

        
print(time_converter('00:00'))


