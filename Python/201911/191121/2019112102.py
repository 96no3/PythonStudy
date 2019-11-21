from turtle import *
Screen()
for i in range(0, 360, 30):  #0度から360度まで30度おきに
    circle(50)               
    left(30)
    
color('green')
for i in range(0, 360, 30):
    circle(30)
    left(30)
    forward(10)

def star(size):
    for i in 1,2,3,4,5:
        forward(size)
        right(180 - 180/5)
        
reset()
star(100)
color('green')
begin_fill()
star(50)
end_fill()

def fractal(size, depth=0):
   if depth <= 0:
      forward(size)
   else:
      fractal(size/3, depth-1)
      left(60) #1/3の長さでフラクタル描画、左に60度向く
      fractal(size/3, depth-1)
      left(-120) #1/3の長さでフラクタル描画、右に120度向く
      fractal(size/3, depth-1)
      left(60) #1/3の長さでフラクタル描画、左に60度向く
      fractal(size/3, depth-1) #1/3の長さでフラクタル描画
      
reset()
fractal(200)
reset()
fractal(200, 1)
reset()
fractal(200, 2)
reset()
fractal(200, 3)
reset()
goto(-100,-100)
clear()
for i in "12345":
    fractal(200, 3)
    left(360/5)
