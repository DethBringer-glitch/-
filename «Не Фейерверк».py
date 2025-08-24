from turtle import *
import random
import time
def amogususalut():
    t.up()
    t.speed(0)
    t.goto(x=random.randint(-250, 250), y=-150)
    t.speed(3)
    t.down()
    t.left(90)
    for i in range(12):
        t.forward(10)
        t.up()
        t.forward(10)
        t.down()
    t.speed(0)
    t.up()
    t.left(120)
    t.forward(10)
    t.right(120)
    t.down()
    t.color(cl_pk())
    t.begin_fill()
    for i in range(5):
        t.right(145)
        t.forward(75)
    t.end_fill()
    time.sleep(3)
    t.clear()
    t.up()
    t.home()
    t.down()
def cl_pk():
    list = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    color = '#'
    for i in range(6):
        color += random.choice(list)
    return color
t = Pen()
t.shape('arrow')
screen = Screen()
screen.screensize(500,320)
screen.setup(500, 320)
screen.bgcolor('#1a155e')
screen.title('Фейерверк')
while True:
    amogususalut()

mainloop()
