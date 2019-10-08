def time_log(func):
    """処理時間を計測するデコレータ関数"""
    def wrapper(*args,**kwargs):
        import datetime
        start = datetime.datetime.today()
        print("\n---start:" + func.__name__)
        res = func(*args,**kwargs)
        end = datetime.datetime.today()
        delta = end - start
        print("\n---end:" + func.__name__,delta,"sec")
        return res
    return wrapper

@time_log
def show(x=9,*,digit=3):
    """九九の表を表示させる関数
       @param x     表示させたい九九の段数（default=9）
       @param digit 表示調整桁数（default=3）"""
    for i in range(1,x+1):
        tmp=str(i).rjust(digit," ")
        print(f"\n{tmp}: ",end="")
        for j in range(1,10):
            result = str(i*j).rjust(digit," ")
            print(f"{result}",end=" ")

show()
show(111)
show(200,digit=4)
