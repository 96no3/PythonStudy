from turtle import *
Screen()
bgcolor('red') # スクリーンの背景色を設定
print(bgcolor())
bgcolor('#4682b4')
bgcolor(0,0,0)
bgcolor(1.0,0.5,0.5)

print(colormode()) # デフォルトは0～1.0
colormode(255) # 256階調でカラーコードを指定
print(colormode())

bgcolor(0x46,0x82,0xb4)
bgcolor(120,0,120)
for i in range(256):
    bgcolor(i,i,i)

for i in range(256):
    bgcolor(i,0,i)

pencolor("blue") # ペンの色を設定
print(pencolor())
