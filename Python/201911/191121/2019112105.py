import turtle

def sample2():
  for i in range(36):
    turtle.forward(10)
    turtle.right(10)
    for j in range(3):
      turtle.forward(50)
      turtle.right(120)

turtle.up()
turtle.goto(0, 50) # 位置の調節
turtle.down()

turtle.tracer(0) # 0:アニメーションなし 1:アニメーションあり
# 一度にフラッシュする頂点数を指定、0の場合はバッファにためておいて、まとめて行う。
# まとまりを超えて再度描画したい場合は1に戻しておかないと表示されないものがある。
sample2()
turtle.update() # TurtleScreen の更新を実行。トレーサーがオフの時に使用。
#turtle.tracer(1) # アニメーションを復活させないと描画されないものがある
#turtle.forward(100)
