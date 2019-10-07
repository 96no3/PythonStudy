# 例外処理
def get(s):
    
    def err():
        raise ValueError
    
    if s == "":
        err()
    elif s[0] == "+":
        return get(s[1:])
    elif s[0] == "-":
        return get(s[1:])
    elif s.isdigit():
        return eval(s)
    err()

print(get("--+-1"))

# リストの演算
[[0]*3]*4

import numpy as np
a= np.array([[0]*4]*3)
a[2][3]=5
a[0]=1

def shift(xs):
    for i in range(len(xs)-1):
        xs[i],xs[i+1]=xs[i+1],x[i]

x=list(range(10))
shift(x)
