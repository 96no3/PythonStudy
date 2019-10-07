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
    n=len(numlist)
    m=len(strlist)
    
    if not n==0:
        for i in range(n):
            swap_flag=False
            for j in range(1,n):
                if function(numlist[j-1],numlist[j]):
                    numlist[j-1],numlist[j]=numlist[j],numlist[j-1]
                    swap_flag=True
            if not swap_flag:
                break
        print(numlist)
            
    if not m==0:
        for i in range(m):
            swap_flag=False
            for j in range(1,m):
                if function(strlist[j-1],strlist[j]):
                    strlist[j-1],strlist[j]=strlist[j],strlist[j-1]
                    swap_flag=True
            if not swap_flag:
                break
        print(strlist)
                    
    return numlist + strlist

print(my_sort4([1,3,"ahg",-8,"king",5,7,"a",9,55,4.74,"world"],lambda a,b:a<b),"\n")
print(my_sort4([1,3,"ahg",-8,"king",5,7,"a",9,55,4.74,"world"],lambda a,b:a>b))
