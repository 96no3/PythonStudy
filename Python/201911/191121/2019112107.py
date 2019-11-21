import turtle

def rtriangle(length, level):
  def tri(length):
    for i in range(3):
      turtle.forward(length)
      turtle.right(120)

  if level > 0:
    tri(length)
    n = length / 2
    turtle.up()
    turtle.forward(n)
    turtle.right(60)
    turtle.down()
    rtriangle(n, level-1)

turtle.tracer(1)
rtriangle(150, 5)
