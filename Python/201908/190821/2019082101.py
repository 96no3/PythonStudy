def CheckEqual(num1,num2,*,prec=1e-3):
    """num1:比較する数1 と num2:比較する数2が近似かどうかを確認する関数
       prec:精度の小数桁数（デフォルトは1/1000,1e-10より小さい場合は1e-10とする）
       返り値 true:近似している　false:近似していない"""
    n=prec
    if prec < 1e-10:
        n=1e-10
        print("Error:precは1e-10より大きい値を設定してください")
        print("invalid:",prec)
    elif prec > 1e-3:
        n=1e-3
        print("Error:precは1e-3より小さい値を設定してください")
        print("invalid:",prec)
    return abs(num1-num2) < n

def MySqrt(num1,num2,*,prec=1e-3):
    """num2:求めたい平方根の数 を num1:予測する平方根の値 から計算する関数
       prec:精度の小数桁数（デフォルトは1/1000,1e-10より小さい場合は1e-10とする）
       返り値 i:近似する平方根の値"""
    
    def Estimate(num1,num2):
        """平方根の近似値を計算する関数
           @param num1 予測する平方根の値
           @param num2 求めたい平方根の数
           @retval     予測する平方根の近似値"""
        return (num1 + num2 / num1) * 0.5

    n=prec
    if prec < 1e-10:
        n=1e-10
        print("Error:precは1e-10より大きい値を設定してください")
        print("invalid:",prec)
    elif prec > 1e-3:
        n=1e-3
        print("Error:precは1e-3より小さい値を設定してください")
        print("invalid:",prec)        

    i = num1    
    while not CheckEqual(i * i, num2,prec=n):
        i = Estimate(i,num2)
    return i


x = int(input("求めたい平方根の数字を入力してください x:"))
y = float(input("予想する平方根の値を入力してください y:"))
precision = float(input("精度の値(1e-3~1e-10)を入力してください prec:"))

print("求める平方根の近似値は:" + str(MySqrt(y,x,prec=precision)))
print('end')
