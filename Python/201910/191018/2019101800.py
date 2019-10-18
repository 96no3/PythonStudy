# iteratorとiterable
"""
next(range(10)) # iteratorではないのでエラー
next([1,2,3])
"""

a=iter(range(10))
next(a)
next(a)
hasattr(a,"__iter__")
hasattr(a,"__next__")

hasattr(range(10),"__iter__")
hasattr(range(10),"__next__")

b=iter([1,2,3])
for i in b:
    print(i)

# ジェネレータ関数
def gen(n):
    for i in range(n):
        yield i*i
        print("再開しました",i)

gen(3)
c=gen(3)
next(c)
next(c)
hasattr(gen(3),"__iter__")
hasattr(gen(3),"__next__")

for i in gen(5):
    print(i)
