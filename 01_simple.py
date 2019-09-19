# coding: utf-8

from graph import *
import math
penColor(255, 255, 255)
penSize(1)
brushColor(126, 188, 209)
rectangle(0, 0, 500, 750)

penColor(255,203,88)
brushColor(242,178,103)
rectangle(0, 105, 500, 350)

penColor("Black")
brushColor(19,166,50)
rectangle(0, 350, 500, 750)
x = 0
for i in range(15):
    x = x +31.25
    penColor("Black")
    line(x, 105, x, 350)

penColor("Black")
brushColor(242,178,103)
polygon( [(312.5, 370), (382, 385), (382, 490), (312.5, 447.5), (312.5, 370) ])


polygon( [(382, 385), (412.5, 360), (412.5,430) , (382,490)])

polygon([(312.5, 370), (355, 320), (382,385), (312.5, 370)])

polygon([(355,320), (382,300),(412.5,360),(382,385),(355,320)])

brushColor(86,86,86)
rectangle(48,435,103,490)

circle(48,444,8)
circle(103,444,8)

moveTo(53,480)

run()