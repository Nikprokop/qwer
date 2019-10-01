# coding: utf-8

from graph import *
import math


def keyPressed(event):
  global dx, dy
  if event.keycode == VK_LEFT:
    dx = -5; dy = 0
  elif event.keycode == VK_RIGHT:
    dx = 5; dy = 0
  elif event.keycode == VK_UP:
    dx = 0; dy = -5
  elif event.keycode == VK_DOWN:
    dx = 0; dy = 5
  elif event.keycode == VK_SPACE:
    dx = dy = 0
  elif event.keycode == VK_ESCAPE:
    close()


def update():
  for k in range(24):
    moveObjectBy(dog[k], dx, dy)


def elips(x,y,a,b):
  q=[]
  n = 50
  for i in range(n):
      q.append((x + a * math.cos(2 * math.pi * i / n), y +b * math.sin(2 * math.pi * i / n)))

  return polygon(q)


  

def elips2(x,y,a,b):
    q=[]
    n = 50
    for i in range(n):
        q.append((x + a * math.cos(2 * math.pi * i / n), y +b * math.sin(2 * math.pi * i / n)))

    polyline(q)
    return polyline(q)
    


penColor(255, 255, 255)
penSize(1)
brushColor(126, 188, 209)
rectangle(0, 0, 500, 750)

penColor(255,203,88)
brushColor(242,178,103)
rectangle(0, 105, 500, 350)

penColor("Black")
brushColor('#66CC66')
rectangle(0, 350, 500, 750)
x = 0
for i in range(15):
    x = x +31.25
    penColor("Black")
    line(x, 105, x, 350)

penColor("Black")
brushColor(242,178,103)
polygon( [(312.5, 370), (382, 385), (382, 490), (312.5, 447.5), (312.5, 370) ])

dx = 0
dy = 0
polygon( [(382, 385), (412.5, 360), (412.5,430) , (382,490)])


polygon([(312.5, 370), (355, 320), (382,385), (312.5, 370)])

polygon([(355,320), (382,300),(412.5,360),(382,385),(355,320)])



brushColor(0,0,0)
q=[]
n = 50
for i in range(n):
    q.append((345 + 20 * math.cos( 2 * math.pi * i / n), 420 + 24 * math.sin(  2 * math.pi * i / n)))

polygon(q)

elips2(324,440,9,3)
elips2(313,453,8,7)
brushColor(87,87,87)
elips(317,445,5,6)
elips2(305,459,8,3)
elips2(298,463,4,4)
elips2(290,467,10,3)
elips2(276,469,7,3)
elips2(265,467,9,1)
elips2(256,467,5,6)
elips2(247,470,7,2)
elips2(239,475,9,4)


brushColor(86,86,86)
penColor(86,86,86)
obj6 = elips(100,480,50,25)
obj7 = elips(100,510,15,35)
obj8 = elips(60,500,15,35)
obj9 = elips(50,535,18,6)
obj10 = elips(90,545,18,6)
obj11 = elips(150,465,30,20)
obj12 = elips(130,457,12,12)
obj13 = elips(170,480,17,21)
obj14 = elips(145,495,5,17)
obj15 = elips(180,510,5,17)
obj16 = elips(171,527,10,4)
obj17 = elips(140,510,10,4)




penColor("Black")
brushColor(242,178,103)
brushColor(86,86,86)
obj22 = rectangle(48,435,103,490)

obj23 = circle(48,444,8)
obj24 = circle(103,444,8)



brushColor(255, 255, 255)
penColor(0,0,0)
obj18 = elips(63,457,6,2)
obj19 = elips(87,457,6,2)
penColor("Black")
brushColor(0,0,0)
obj20 = circle(63,457,2)
obj21 = circle(87,457,2)

obj1 = line(65,477,85,477)
brushColor(255,255,255)
obj2 = polygon([(65,477), (63,472), (61,481), (65,477)])
obj3 = polygon([(85,477), (87,472), (89,481), (85,477)])
obj4 = line(61,481,59,485)
obj5 = line(89,481,91,485)




dog = [obj1, obj2, obj3, obj4, obj5, obj6, obj7, obj8, obj9, obj10, obj11, obj12, obj13, obj14,
         obj15, obj16, obj17, obj18, obj19, obj20, obj21, obj22, obj23, obj24]

onKey(keyPressed)
onTimer(update,50)

run()
