''' https://py.checkio.org/en/mission/sun-angle/
sun_angle("07:00") == 15
sun_angle("12:15"] == 93.75
sun_angle("01:23") == "I don't see the sun!"
'''

def sun_angle(time):
    hour = time[0:2]
    minute = time[3:5]

    print (hour)
    print (minute)

    time = int(hour) * 60 + int(minute)
    print (time)


    if (time < 360 or time > 1080):
        return ("I don't see the sun!")

    angle = ((time - 360) / 4.00)
    #angle = "{:.2f}".format(angle)

    return angle


print(sun_angle('12:15'))
