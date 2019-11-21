import turtle

def move(x, y):
  turtle.up()
  turtle.goto(x, y)
  turtle.down()
  
def tree(length, level):
  if level > 0:
    #print("in")
    x, y = turtle.position()
    a = turtle.heading() # タートルの現在の向きを返す
    # draw left node
    #print("left",x,y,a,length,level)
    turtle.left(18)
    turtle.forward(length)
    tree(length-10, level-1)

    # draw right node
    #print("right",x,y,a,length,level)
    move(x, y)
    turtle.setheading(a)
    turtle.right(18)
    turtle.forward(length)
    tree(length-10, level-1)

turtle.tracer(1)
move(0, -100)
turtle.setheading(90)
tree(60, 5)
