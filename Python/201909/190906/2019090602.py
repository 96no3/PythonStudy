def ascending(a,b):
    return a<b

def descending(a,b):
    return a>b

def my_sort(xs,function):
    tmplist = xs.copy()
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

def my_sort4(xs,function):
    tmplist = xs.copy()
    numlist = []
    strlist = []
    for i in tmplist:
        if isinstance(i,(int,float)):
            numlist.append(i)
        elif isinstance(i,str):
            strlist.append(i)
        else:
            raise ValueError(i,"は不正な値です")    
                    
    return my_sort(numlist,function) + my_sort(strlist,function)


print(my_sort4([1,3,"ahg",-8,"king",5,7,"a",9,55,4.74,"world"],ascending),"\n")
print(my_sort4([1,3,"ahg",-8,"king",5,7,"a",9,55,4.74,"world"],descending))
