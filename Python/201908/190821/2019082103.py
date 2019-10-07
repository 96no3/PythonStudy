import sys

# _関数内処理用のメンバ関数
def _Eq(x,y,prec):
    """num1:比較する数1 と num2:比較する数2が近似かどうかを確認する関数内処理用関数
       prec:精度の小数桁数（デフォルトは1/1000,1e-10より小さい場合は1e-10とする）
       返り値 true:近似している　false:近似していない""" 
    return abs(x-y) < prec

def _FixPrec(prec):
    """precが有効かどうかを確認する関数内処理用関数
       prec:精度の小数桁数（デフォルトは1/1000,1e-10より小さい場合は1e-10とする）
       返り値 prec:精度""" 
    if prec < 1e-10:
        print("invalid:",prec)
        prec=1e-10
        
    elif prec > 1e-3:
        print("invalid:",prec)
        prec=1e-3
        
    return prec

def CheckEqual(num1,num2,*,prec=1e-3):
    """num1:比較する数1 と num2:比較する数2が近似かどうかを確認する関数
       prec:精度の小数桁数（デフォルトは1/1000,1e-10より小さい場合は1e-10とする）
       返り値 true:近似している　false:近似していない"""    
    return _Eq(num1,num2,_FixPrec(prec))

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

    n=_FixPrec(prec)       

    i = num1    
    while not _Eq(i * i, num2,n):
        i = Estimate(i,num2)
    return i


x = float(input("求めたい平方根の数字を正の数で入力してください x:"))

if x<0:
    print("Error:",x)
    sys.exit(1)
    print("正の整数として実行します")
    x=abs(x)

y = float(input("予想する平方根の値を入力してください y:"))
precision = float(input("精度の値(1e-3~1e-10)を入力してください prec:"))

print("求める平方根の近似値は:" + str(MySqrt(y,x,prec=precision)))
print('end')
