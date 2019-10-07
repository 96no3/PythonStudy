def add_n(num):
    # 高階関数かつクロージャー
    def internal(x):
        return x + num;
    return internal

f=add_n(100)
print(f(4))

g=add_n(-10)
print(g(20))

eval("1+5+9")
eval("input('test:')")

def test(a,b):
    expr = input("式を入力してください：")
    return eval(expr)

test(5,10)

map(lambda a,b:a+b,["Hello","World"],["!","!!"])

import math
list(map(math.sqrt,range(10)))

import random
random.randint(2,10)
x=[]
x.append(3)

list(map(lambda x:random.randint(2,10),range(40)))

for x in map(lambda x:random.randint(2,10),range(4)):
    print(x)

map(print,range(10))
list(map(print,range(10)))

for i in map(print,range(10)):
    pass


