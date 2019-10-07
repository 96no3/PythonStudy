import math

x = int(input("求めたい平方根の数字を入力してください x:"))
y = int(input("予想する平方根の値を入力してください y:"))

ans = math.sqrt(x)
print("求める平方根の値は:" + str(ans))

print("予想値:" + str(y) + " を用いて近似値を計算します")
while True:
    i = y * y
    if int(i) == x:
        print("求める平方根の近似値は:" + str(y))
        break
    else:
        y = (y + x / y) * 0.5
        print("予測値を" + str(y) + " として再計算します")

print('end')
