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

def err(message=""):
    raise ValueError(message)
        
def is_int(a):    
    return isinstance(a,int)

def generate(start,stop,digit,mode):
    """表示形式を変える処理をする関数オブジェクトを返す高階関数
       @param start 表示させたい九九の開始段数（default=１）
       @param stop  表示させたい九九の終わり段数（default=9）
       @param digit 表示調整桁数（default=3）
       @param mode  表示形式のモード番号
       @return proc 九九表示関数オブジェクト"""
    def proc():
        if mode == 0:
            for i in range(start,stop+1):
                tmp = str(i).center(digit," ")
                print(f"\n****{tmp}の段"+"*"*20)
                for j in range(1,10):
                    if j % 3 == 0:
                        tmp = " ||\n"
                    else:
                        tmp = " || "                    
                    result = str(i*j).center(digit," ")
                    print("%03s" % str(i) + " x " + f"{j}" + " = "\
                          + f"{result}",end=tmp)
        else:
            for i in range(start,stop+1):
                tmp=str(i).rjust(digit," ")
                print(f"\n{tmp}: ",end="")
                for j in range(1,10):
                    result = str(i*j).rjust(digit," ")
                    print(f"{result}",end=" ")                
    return proc

def check(xs,digit,mode):
    start,stop = 1,9
    n = len(xs)
    if n == 0 or n > 2 or not is_int(xs[0]) or xs[0]<=0:
        err()
    elif n == 1:
        stop = xs[0]
    else: # n == 2
        if xs[1] <= xs[0]:
            err()
        else:
            start = xs[0]
            stop = xs[1]
    f = generate(start,stop,digit,mode)
    return f

@time_log
def show(*xs,*,digit=3,mode=0):
    """九九の表を表示させる関数
       @param xs    表示させたい九九の段数（デフォルトで1～9の段）
                    引数1つで終わりの段指定、引数2つで開始と終わりの段指定
       @param digit 表示調整桁数（default=3）
       @param mode  表示形式の変更（default=0）
                  =0    例:1 x 1 = 1 ||1 x 2 = 2 || ･･･
                  0以外 例:1: 1 2 3 4 ･･･ """
    if not is_int(digit) or not is_int(mode):
        err()
    f=check(xs,digit,mode)
    f()
        
show()
show(mode=1)
show(15)
show(2,4)
show(190,200,digit=4)
show(190,200,digit=4,mode=1)
