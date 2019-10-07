def make(init=0):
    cnt = init

    def set(n):
        nonlocal cnt
        cnt = n

    def get():
        return cnt
    

    def inc(x=1):
        nonlocal cnt  # nonlocalがなければUnboundLocalError
        cnt += x    

    def dec(x=1):
        nonlocal cnt
        cnt -= x     
    
    return (set,get,inc,dec)

(setter1,getter1,inc1,dec1) = make()
(setter2,getter2,inc2,dec2) = make()

setter1(3)
print("cnt1 =",getter1(),"cnt2 =",getter2())
inc1(4)
print("cnt1 =",getter1(),"cnt2 =",getter2())
dec2(3)
print("cnt1 =",getter1(),"cnt2 =",getter2())














