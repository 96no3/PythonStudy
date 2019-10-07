def descending(a,b):
    """<高階関数>引数のtypeを調べて降順確認を行う関数
       @param a　int,float,str型の入力値
       @param b　int,float,str型の入力値
       @retval True       ソートを行う
       @retval False,None ソートを行わない"""
    if not(isinstance(a,(int,float)) or isinstance(b,(int,float))\
       or isinstance(a,str) or isinstance(b,str)):
        raise ValueError(i,"は不正な値です")
    
    if isinstance(a,(int,float)) and isinstance(b,(int,float)):
        return a<b
    elif isinstance(a,str) and isinstance(b,str):
        return a<b
    elif isinstance(a,str) and isinstance(b,(int,float)):
        return True
        
def ascending(a,b):
    """<高階関数>引数のtypeを調べて昇順確認を行う関数
       @param a　int,float,str型の入力値
       @param b　int,float,str型の入力値
       @retval True       ソートを行う
       @retval False,None ソートを行わない"""
    if not(isinstance(a,(int,float)) or isinstance(b,(int,float))\
       or isinstance(a,str) or isinstance(b,str)):
        raise ValueError(i,"は不正な値です")
    
    if isinstance(a,(int,float)) and isinstance(b,(int,float)):
        return a>b
    elif isinstance(a,str) and isinstance(b,str):
        return a>b
    elif isinstance(a,str) and isinstance(b,(int,float)):
        return True
        
def my_sort(xs,function):
    """ソートを行う関数
       @param xs       ソートを行うリスト
       @param function ソート判定の関数オブジェクト
       @return tmplist ソート済みのリスト"""
    tmplist = xs.copy() # xs自身を書き換えると破壊的関数になる→他の環境を汚す
    n=len(tmplist)
    for i in range(n-1):
        swap_flag=False
        for j in range(1,n-i):
            if function(tmplist[j-1],tmplist[j]):
                tmplist[j-1],tmplist[j]=tmplist[j],tmplist[j-1]
                swap_flag = True
        if not swap_flag:
            break
    print(tmplist)
    return tmplist

print(my_sort([1,3,"ahg",-8,"king",5,7,"a",9,55,4.74,"world"],ascending),"\n")
print(my_sort([1,3,"ahg",-8,"king",5,7,"a",9,55,4.74,"world"],descending))
