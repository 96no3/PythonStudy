import math

def CheckEqual(num1,num2):
    return abs(num1-num2) < 1e-15   

def Estimate(num1,num2):
    return (num1 + num2 / num1) * 0.5

x = int(input("求めたい平方根の数字を入力してください x:"))
y = int(input("予想する平方根の値を入力してください y:"))

print("求める平方根の値は:" + str(math.sqrt(x)))

print("予想値:" + str(y) + " を用いて近似値を計算します")
while not CheckEqual(y * y, x):
    y = Estimate(y,x)
    print("予測値を" + str(y) + " として再計算します")
    
print("求める平方根の近似値は:" + str(y))
print('end')
