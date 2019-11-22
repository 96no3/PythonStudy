from turtle import *
Screen()
onscreenclick(goto) # 返り値は中心（0,0）とするスクリーン座標のタプル
pencolor("green")
onkeypress(penup,"Up")
onkeypress(pendown,"Down")
onkeypress(lambda :forward(50),"Right")
onkeypress(lambda :backward(50),"Left")
listen() # onkeyイベントを有効化（TurtleScreen にフォーカス）
