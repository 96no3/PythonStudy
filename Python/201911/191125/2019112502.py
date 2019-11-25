import turtle

class Square:    
    def __init__(self, x, y, size):
        self.size = size
        self.x = x
        self.y = y

    def drawself(self):
        turtle.goto(self.x - self.size // 2, self.y - self.size // 2)
        turtle.fillcolor(turtle.pencolor())
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(self.size)
            turtle.left(90)
        turtle.end_fill()

class Circle:    
    def __init__(self, x, y, size):
        self.size = size*0.5
        self.x = x
        self.y = y

    def drawself(self):
        turtle.goto(self.x, self.y - self.size // 2)
        turtle.fillcolor(turtle.pencolor())
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

class Draw:
    def __init__(self):
        self.__speed = 10
        self.__pensize = 1
        self.__stampsize = 20
        turtle.Screen()
        turtle.shape("circle")
        turtle.turtlesize(0.1,0.1,self.__pensize)
        turtle.tracer(0)
        turtle.listen()
        turtle.onkeypress(self.move(0,-1), "Down")
        turtle.onkeypress(self.move(0,1), "Up")
        turtle.onkeypress(self.move(-1,0), "Left")
        turtle.onkeypress(self.move(1,0), "Right")
        turtle.onkeypress(self.reset(), "z")
        turtle.onkeypress(turtle.clear, "c")
        turtle.onkeypress(lambda :turtle.pencolor("red"), "r")
        turtle.onkeypress(lambda :turtle.pencolor("blue"), "b")
        turtle.onkeypress(lambda :turtle.pencolor("green"), "g")
        turtle.onkeypress(turtle.penup, "u")
        turtle.onkeypress(turtle.pendown, "d")
        turtle.onkeypress(self.setspeed(-1), "Shift_L")
        turtle.onkeypress(self.setspeed(1), "Shift_R")
        turtle.onkeypress(self.setsize(-1), "Control_L")
        turtle.onkeypress(self.setsize(1), "Control_R")
        turtle.onkeypress(self.setstampsize(-1), "Alt_L")
        turtle.onkeypress(self.setstampsize(1), "Alt_R")
        turtle.onkeypress(self.stamp(0), "0")
        turtle.onkeypress(self.stamp(1), "1")
        turtle.ondrag(turtle.goto)
        turtle.onscreenclick(turtle.setpos)

    def move(self,x,y):
        def f():
            nowX,nowY = turtle.position()
            turtle.goto(nowX+x*self.__speed, nowY+y*self.__speed)
        return f

    def reset(self):
        def f():
            turtle.penup()
            turtle.goto(0,0)
            turtle.pendown()
            self.__pensize = 1
            self.__speed = 10
            turtle.pensize(self.__pensize)
            turtle.turtlesize(0.1,0.1,self.__pensize)
        return f       

    def nextFrame(self):
        turtle.update()
        turtle.ontimer(lambda: self.nextFrame(), 100)

    def setspeed(self,n):
        def f():
            if self.__speed == 1 and n < 0:
                return None
            self.__speed += n
            print("speed:",self.__speed)
        return f

    def setsize(self,n):
        def f():
            if self.__pensize == 1 and n < 0:
                return None
            self.__pensize += n
            print("pen:",self.__pensize)
            turtle.pensize(self.__pensize)
            turtle.turtlesize(outline=self.__pensize)
        return f

    def setstampsize(self,n):
        def f():
            if self.__stampsize == 1 and n < 0:
                return None
            self.__stampsize += n
            print("stamp:",self.__stampsize)
        return f

    def stamp(self,shape):
        def f():
            if shape == 0:
                x,y = turtle.position()
                s = Square(x,y,self.__stampsize)
                s.drawself()
            elif shape == 1:
                x,y = turtle.position()
                s = Circle(x,y,self.__stampsize)
                s.drawself()
        return f

draw = Draw()
draw.nextFrame()
