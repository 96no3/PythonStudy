import math

map(math.sqrt,[4,5,6])
tuple(map(math.sqrt,[4,5,6]))
list(map(math.sqrt,[4,5,6]))
list(map(lambda *xs:xs,[1,4,6,8],[2,4,6]))
list(map(lambda *xs:xs,[1,4,6,8],[2,4,6],[]))
list(map(lambda *xs:xs,[1,4,6,8],[2,4,6],range(1000)))
list(map(lambda *xs:xs,[1,4,6,8],[2,4,6],range(1000,2000)))

import functools as ft
ft.reduce(lambda *xs:xs,[1,3,5,7,9])
ft.reduce(lambda a,b:f"{a}:{b}",[1,3,5,7,9])
ft.reduce(lambda a,b:[a,b],[1,3,5,7,9])
ft.reduce(lambda a,b:a+b,[1,3,5,7,9])
ft.reduce(lambda a,b:a+b,['a','b','x','yz'])

list(map(ord,"abcdefg"))
list(map(ord,"0123456789"))
list(map(int,"0123456789"))

def test():
    src=input("> ")
    src=tuple(map(int,src.split(",")))
    print(src)

    
