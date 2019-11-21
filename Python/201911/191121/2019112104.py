from turtle import *

textinput("入力してください","name") # 入力ダイアログ（str型）
numinput("入力してください","number") # 入力ダイアログ（float型）

while True:
    s = textinput("input","cmd")
    if s == "end":
        break
    forward(int(s))
    left(90)

onscreenclick(lambda *x:print(x)) # マウスで左クリックした座標を表示
