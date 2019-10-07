### 数が近似かどうかを確認する関数.
# @param num1 比較する数1
# @param num2 比較する数2
#
# @retval true   2数が近似している
# @retval false  2数が近似していない
###
def CheckEqual1(num1,num2):
    return abs(num1-num2) < 1e-15

def CheckEqual2(num1,num2,prec=1e-3):
    """num1:比較する数1 と num2:比較する数2が近似かどうかを確認する関数
       prec:精度の小数桁数（デフォルトは1/1000,15桁より大きい場合は15とする）
       返り値 true:近似している　false:近似していない"""
    if prec < 1e-15:
        prec = 1e-15
    return abs(num1-num2) < prec

def MySqrt(num1,num2,prec=1e-3):
    """num2:求めたい平方根の数 を num1:予測する平方根の値 から計算する関数
       prec:精度の小数桁数（デフォルトは1/1000,15桁より大きい場合は15とする）
       返り値 i:近似する平方根の値"""
    if prec < 1e-15:
        prec = 1e-15

    def Estimate(num1,num2):
        """平方根の近似値を計算する関数
           @param num1 予測する平方根の値
           @param num2 求めたい平方根の数
           @retval     予測する平方根の近似値"""
        return (num1 + num2 / num1) * 0.5    

    i = num1    
    while not CheckEqual2(i * i, num2,prec):
        i = Estimate(i,num2)
    return i

x = int(input("求めたい平方根の数字を入力してください x:"))
y = int(input("予想する平方根の値を入力してください y:"))

print("求める平方根の近似値は:" + str(MySqrt(y,x,1e-10)))
print('end')
