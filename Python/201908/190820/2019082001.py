def AddOne(i):
    return i+1

def SayHello():
    print("Hello World")

def CheckEqual(num1,num2):
    if abs(num1-num2) <= 1e-1:
        print("xとyの値は近似しています")
    else:
        print("xとyの値は近似していません")

def Estimate(num1,num2):
    return (num1 + num2 / num1) * 0.5

SayHello()
x = float(input('Please input x:'))
print("入力値に+1した値："+str(AddOne(x)))

y = float(input('Please input y:'))
print(Estimate(x,y))
CheckEqual(x,y)

print('Finish')
