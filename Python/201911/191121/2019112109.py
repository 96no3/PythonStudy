import turtle

def leaf(n, pencolor, brushcolor):
  def cir():
    for i in range(9):
      turtle.forward(n)
      turtle.right(10)

  a = turtle.heading()
  turtle.color(brushcolor)
  turtle.begin_fill()
  cir()
  turtle.right(90)
  cir()
  turtle.end_fill()

  turtle.setheading(a)
  turtle.color(pencolor)
  cir()
  turtle.right(90)
  cir()

def flower(x, y, size, color_set):
  turtle.up()
  turtle.goto(x, y)
  turtle.down()
  turtle.setheading(90)
  turtle.color(color_set[0])
  turtle.forward(size * 2)
  turtle.right(30)
  leaf(size, color_set[0], color_set[0])
  turtle.setheading(90)
  turtle.forward(size * 14)

  for i in range(9):
    leaf(size, color_set[1], color_set[2])
    turtle.right(10)
  
turtle.tracer(0)
flower(-100, -120, 7, ("lightgreen",  "mistyrose", "lightpink"))
flower(0,    -120, 4, ("greenyellow", "lemonchiffon", "gold"))
flower(100,  -120, 8, ("palegreen", "paleturquoise", "lightblue"))
turtle.update()
