import turtle
t = turtle.Pen()
t.color('green')
t.up()
t.goto(-250,200)
t.down()
for i in range(4):
    t.forward(150)
    t.left(90)
r = turtle.Pen()
r.speed(250)
r.up()
r.goto(300,-225)
r.down()
for i in range(36):
    y = turtle.Pen()
    y.speed(250)
    y.pensize(10)
    y.color('yellow')
    y.up()
    y.goto(250,300)
    y.down()
    y.fillcolor('yellow')
    y.begin_fill()
for i in range(36):
     y.circle(75.50000000000)
     y.left(50)
y.end_fill()

j = turtle.Pen()
j.speed(2500)
j.up()
j.goto(-300,-225)
j.down()
e = 1
for i in range(245):
    j.forward(e)
    j.left(75)
    e+=1


turtle.mainloop()