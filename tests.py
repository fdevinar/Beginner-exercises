''' https://py.checkio.org/en/mission/sun-angle/
sun_angle("07:00") == 15
sun_angle("12:15"] == 93.75
sun_angle("01:23") == "I don't see the sun!"
'''

def sun_angle(time):
    hour = time[1:2]
    minute = time[3:5]

    time = int(hour) * 60 + int(minute)

    #print (hour ,minute)

    #print (time)

    # tratar horario noturno
    # 2 casas decimais
    
    angle = (time - 360 / 4.00)

    return angle


print(sun_angle('12:15'))
