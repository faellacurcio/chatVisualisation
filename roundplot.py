import numpy as np
import matplotlib.pyplot as plt
import math
import sys
import os
import time
from datetime import datetime

plt.rcParams["axes.axisbelow"] = False

deltaMinutes = 120  # Number of minumum seconds before new point 1800 = 30min
alpha = 0.2
color = 'g'
font = {'family': 'normal',
        'weight': 'bold',
        'size': 22}

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


cmdargs = list(sys.argv)

ax = plt.subplot()
if( len(cmdargs) > 1):
    ax = plt.subplot(111, projection="polar")
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.set_rlabel_position(0)
ax.set_xticklabels(['Jan', 'Fev', 'Mar', 'Abr', 'Jun', 'Jul', 'Ago', 'Set',
                    'Out', 'Nov', 'Dez'])
ax.axes.get_xaxis().set_ticks(np.linspace(0, 2*math.pi, 12))
ax.axes.get_yaxis().set_ticks([200+60, 395, 200+720, 1185, 200+1380])
ax.axes.get_yaxis().set_ticklabels(['1:00am', 'sunrise', '12:00pm', 'sunset', '23:00pm'], zorder=4)

# Plot the Ring/Strip of sunlight
circle = plt.Circle(
    (0, 0),
    1185,
    transform=ax.transData._b,
    color="red",
    alpha=0.1)
ax.add_artist(circle)

circle = plt.Circle(
    (0, 0),
    395,
    transform=ax.transData._b,
    color="white",
    alpha=1,
    zorder=1)
ax.add_artist(circle)

#Set the color of markers
c = plt.scatter(0, 0)
c.set_color('w')

filesFound = False

# Go through all .txt files that comply with 
for file in os.listdir("./"):
    if file.endswith(".txt"):
        filesFound = True
        
        f = open(os.path.join("./", file))

        lastmessagetime = 0
        line = ' '
        while(line):
            line = f.readline()
            if(len(line) > 2):
                if(line[2] == '/'):
                    text_date = line.split(' - ')[0]
                    date = datetime.strptime(text_date, "%d/%m/%Y %H:%M")
                    if(lastmessagetime + deltaMinutes > time.mktime(date.timetuple()) ):
                        pass
                    else:
                        c = plt.scatter(
                            (date.day.real/30)*(date.month.real*(2*math.pi/12)),
                            200+(date.hour.real*60) + (date.minute.real),
                            cmap=plt.cm.hsv,
                            zorder=2
                            )
                        c.set_color(color)
                        c.set_alpha(alpha)
                        lastmessagetime = time.mktime(date.timetuple())
                else:
                    pass

        # plt.show()
        plt.savefig(file[25:-4]+'.png', dpi=300)

if(not filesFound):
    print("No files found, exiting program...")


# for point in range(100):
#     c = plt.scatter(0.06*point, 1*point, cmap=plt.cm.hsv)
#     c.set_color('g')
#     c.set_alpha(point/100)

