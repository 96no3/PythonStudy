def CheckEqual(num1,num2):
    return abs(num1-num2) < 1e-15   

def Estimate(num1,num2):
    return (num1 + num2 / num1) * 0.5

def MySqrt(num1,num2):
    i = num1
    
    while not CheckEqual(i * i, num2):
        i = Estimate(i,num2)
    return i

x = int(input("求めたい平方根の数字を入力してください x:"))
y = int(input("予想する平方根の値を入力してください y:"))

num = 0
print("求める平方根の近似値は:" + str(MySqrt(y,x)))
print('end')
