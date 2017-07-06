import numpy as np
import matplotlib.pyplot as plt
import math
import sys
import time
from datetime import datetime

deltaseconds = 3600  # Number of minumum seconds before new point 1800 = 30min
alpha = 0.2
color = 'g'
font = {'family': 'normal',
        'weight': 'bold',
        'size': 22}
# Coletar pontos por hora
# Densidade de pontos daquela hora representado por alpha


def insertPoint(text, plt):
    if(len(text) > 2):
        if(text[0] == '2' and text[1] == '0'):
            text_date = text.split(' - ')[0]
            date = datetime.strptime(text_date, "%Y-%m-%d, %I:%M %p")
            c = plt.scatter(
                date.day*(date.month*(2*math.pi/12)/30),
                (date.hour*60) + (date.minute),
                cmap=plt.cm.hsv
                )
            c.set_color(color)
            c.set_alpha(alpha)
        else:
            pass


if(len(sys.argv) > 0):
    ax = plt.subplot()
    # ax = plt.subplot(111, projection="polar")
    # ax.set_theta_zero_location("N")
    ax.set_xticklabels(['Jan', 'Fev', 'Mar', 'Abr', 'Jun', 'Jul', 'Ago', 'Set',
                        'Out', 'Nov', 'Dez'])
    # ax.set_theta_direction(-1)
    ax.axes.get_xaxis().set_ticks(np.linspace(0, 2*3.14, 12))
    ax.axes.get_yaxis().set_ticks([200+60, 200+720, 200+1380])
    ax.axes.get_yaxis().set_ticklabels(['1:00am', '12:00pm', '23:00pm'])
    # ax.set_rlabel_position(0)

    # circle = plt.Circle(
    #     (0, 0),
    #     1280,
    #     transform=ax.transData._b,
    #     color="red",
    #     alpha=0.1)
    # ax.add_artist(circle)
    #
    # circle = plt.Circle(
    #     (0, 0),
    #     680,
    #     transform=ax.transData._b,
    #     color="white",
    #     alpha=1)
    # ax.add_artist(circle)

    c = plt.scatter(0, 0)
    c.set_color('w')
    try:
        # f = open("MariaEduardaFarias.txt")
        # f = open("AnaJulia.txt")
        f = open("VicOliveira.txt")
    except():
        print("Couldn't open file")
    lastmessagetime = 0
    line = ' '
    while(line):
        line = f.readline()
        if(len(line) > 2):
            if(line[0] == '2' and line[1] == '0'):
                text_date = line.split(' - ')[0]
                date = datetime.strptime(text_date, "%Y-%m-%d, %I:%M %p")
                if(
                    lastmessagetime + deltaseconds
                    >
                    time.mktime(date.timetuple())
                ):
                    pass
                else:
                    c = plt.scatter(
                        (date.day.real/30)*(date.month.real*(2*math.pi/12)),
                        200+(date.hour.real*60) + (date.minute.real),
                        cmap=plt.cm.hsv
                        )
                    c.set_color(color)
                    c.set_alpha(alpha)
                    lastmessagetime = time.mktime(date.timetuple())
            else:
                pass

    plt.show()


# for point in range(100):
#     c = plt.scatter(0.06*point, 1*point, cmap=plt.cm.hsv)
#     c.set_color('g')
#     c.set_alpha(point/100)

# print([
#     'day:',
#     (date.day.real),
#     'month:',
#     (date.month.real),
#     'year:',
#     (date.year.real),
#     'hour:',
#     (date.hour.real),
#     'line:',
#     (text_date),
#     ])
