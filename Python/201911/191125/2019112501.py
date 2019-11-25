from turtle import *

def move(x,y):
    nowX,nowY = position()
    goto(nowX + x, nowY + y)

def reset():
    penup()
    setpos(0,0)
    pendown()

Screen()
shape('turtle')
onkeypress(lambda :move(0,-20), "Down")
onkeypress(lambda :move(0,20), "Up")
onkeypress(lambda :move(-20,0), "Left")
onkeypress(lambda :move(20,0), "Right")
onkeypress(reset, "z")
onkeypress(clear, "c")
onkeypress(lambda :pencolor("red"), "r")
onkeypress(lambda :pencolor("blue"), "b")
onkeypress(lambda :pencolor("green"), "g")
onkeypress(penup, "u")
onkeypress(pendown, "d")
listen()
done()
