"1010"[::-1]

[int(s) for s in "1010"[::-1]]

zip(range(4),[int(s) for s in "1010"[::-1]])
[*zip(range(4),[int(s) for s in "1010"[::-1]])]
[*enumerate([int(s) for s in "1010"[::-1]])]
[2 ** a * x for a,x in enumerate([int(s) for s in "1010"[::-1]])]
sum([2 ** a * x for a,x in enumerate([int(s) for s in "1010"[::-1]])])

# ジェネレータ式
sum(2 ** a * x for a,x in enumerate(int(s) for s in "1010"[::-1]))

(x*x for x in range(10))
a=(x*x for x in range(10))
next(a)
next(a)

def f(x):
    pass

f(x*x for x in range(10))

def g(a,b):
    pass

g((x*x for x in range(10)),0)

# 集合(セット)内包表記
{x*x for x in range(10)}
7 in {x*x for x in range(10)}
49 in {x*x for x in range(10)}
{ x+y for x in [1,2,3] for y in [1,2,3] }
[ x+y for x in [1,2,3] for y in [1,2,3] ]

# 辞書内包表記
{"abc":10,10:-10}["abc"]
{"abc":10,10:-10}[10]
{str(x):x*x for x in range(10)}
{str(x):x*x for x in range(10)}["5"]

# forループ、map,filter → リスト内包
data = []
for i in range(1,6):
    data.append(i * 2)
print(data)

data=[i*2 for i in range(1,6)]
print(data)

data = list(map(lambda x:x*2,range(1,6)))
print(data)

data2 = [x for x in range(1,6) if x%2 == 0 ]
print(data2)

data2 = list(filter(lambda x:x%2==0,range(1,6)))
print(data2)

# リスト内包と三項演算子
res=["Fizz Buzz" if i%15==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else str(i)
     for i in range(1,21)]
print("\n".join(res))
