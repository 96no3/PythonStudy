import turtle

def spiral(size, angle):
  if size < 100:
    turtle.forward(size)
    turtle.right(angle)
    spiral(size+2, angle)

turtle.tracer(0)
spiral(0, 90)

turtle.up()
turtle.goto(140, 20)
turtle.down()
spiral(0, 70)
