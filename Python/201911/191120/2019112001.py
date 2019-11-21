from turtle import *
color('red', 'yellow') # ペンの色と塗りつぶしの色を設定
begin_fill() # これ以降の図を満たす
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill() # 満たす図の末尾に呼び、begin_fill()の後に記述
done() # イベントループの開始
