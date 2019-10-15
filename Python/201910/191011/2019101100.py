"+".join(["-"*w for w in [1,2,2,2,2,2,3]])
"+"+"+".join(["-"*w for w in [1,2,2,2,2,2,3]])+"+"
def f(xs,s):
    return s+s.join(xs)+s
f(["-"*w for w in [1,2,2,2,2,2,3]],"+")
f(["-"*w for w in [1,2,2,2,2,2,3]],"|")

# 辞書内包表記
{x:str(x*x) for x in range(10)}

# 集合内包表記
{x for x in range(100) if x%5==0 if x%7==0}

# ジェネレータ内包表記
(x*x for x in range(10))

tuple(x*x for x in range(10))
sum(x*x for x in range(10))
for i in (x*x for x in range(10)):
    print(i)
