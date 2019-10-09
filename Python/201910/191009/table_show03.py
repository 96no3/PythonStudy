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
def show(first=1,end=9,*,mode=0):
    r=range(first,end+1)
    column=[i for i in r]
    table=[[i*j for i in r] for j in r]
    ps=[len(str(x)) for x in table[-1]]
    left=len(str(table[-1][0]))
    str_line=""
    str_table=""
    str_table_list=["|".join(line)
                    for line in [["%*d"%v for v in zip(ps,table[n])]
                                 for n in range(len(column))]]
    
    str_column=" "*left + "  "
    for x in zip(ps,column):
        str_column = str_column + "%*d"%x + " "        

    if mode == 0:
        str_line=" "*left + " "
    str_line = str_line + "+"
    for i in ps:
        str_line = str_line + "-"*i + "+"        
    
    # 1段目
    if mode == 0:
        str_table = str_column + "\n"
    
    # 2段目以降
    for n in range(len(column)):
        str_table = str_table + str_line + "\n"
        if mode == 0:
            str_table = str_table + "%*d "%(left,column[n])        
        str_table = str_table + "|" + str_table_list[n] + "|\n"
    str_table = str_table + str_line + "\n"
    print(str_table)

show()
#show(5)
#show(4,10)
show(mode=1)
#show(10,15,mode=1)
                
            
        
    
        
        
        
    
        
