import turtle

turtle.Screen() # スクリーン作成

# 正方形の描画
vertex = 4
for _ in range(vertex):
    turtle.forward(100) # 中心が(0,0)右が+
    turtle.left(360 / vertex) # 90度左に回転

turtle.reset() # (0,0)に戻す

def rect(n,length):
    """正ｎ角形を描画する関数
       @param n      頂点数
       @param length 一辺の長さ"""
    for _ in range(n):
        turtle.forward(length) # 中心が(0,0)右が+
        turtle.left(360 / n) # 90度左に回転

rect(5,100)
rect(40,15) # 円の表現
turtle.circle(20)
print(turtle.position()) # 現在の座標
