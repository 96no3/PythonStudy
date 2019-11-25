from turtle import *

Screen()
d=5 # 一回のキー操作で進む距離（ピクセル数）

# カーソルを移動させるコールバック関数を生成する高階関数
def mover(cx,cy):
    def callback():
        x,y=position()
        goto(x+cx*d,y+cy*d)
    return callback

onkeypress(mover(0,-1), "Down")
onkeypress(mover(0,1), "Up")
onkeypress(mover(-1,0), "Left")
onkeypress(mover(1,0), "Right")
del mover # 後々使わない関数は名前を削除して外部からアクセスできなくするとよい

onkeypress(clear, "c")
onkeypress(penup, "u")
onkeypress(pendown, "d")

onkeypress(lambda :pencolor("red"), "r")
onkeypress(lambda :pencolor("green"), "g")
onkeypress(lambda :pencolor("blue"), "b")

def reset_position():
    penup()
    setpos(0,0)
    pendown()

onkeypress(reset_position, "z")
del reset_position

def draw_by_drag(a,b):
    print("ondrag:",a,b) # デバッグ出力
    tracer(0) # 描画の遅延を一旦0にしてから
    goto(a,b) # 線を描画し、
    tracer(1) # その後、通常の描画モードに戻す
    
ondrag(draw_by_drag)
onscreenclick(setpos)

listen()
