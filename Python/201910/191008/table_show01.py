# table作成show関数
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
def show(first=1,end=9):
    column=[i for i in range(first,end+1)]
    table=[[i*j for i in range(first,end+1)] for j in range(first,end+1)]
    digit=[len(str(table[-1][i])) for i in range(len(column))]
    left=len(str(table[-1][0]))
    
    str_column="".join(" "*left + "  ")
    for x in zip(digit,column):
        str_column = str_column + "%*s"%x + " "        
        
    str_line="".join(" "*left + " +")
    for i in digit:
        str_line = str_line + "-"*i + "+"        
    
    # 1段目
    print(str_column)
    # 2段目以降
    for n in range(len(column)):
        print(str_line)
        print("%*d"%(left,column[n]),end=" |")
        for v in zip(digit,table[n]):
            print("%*d"%v,end="|")
        print("")

show()
show(5)
show(4,10)
                
            
        
    
        
        
        
    
        
