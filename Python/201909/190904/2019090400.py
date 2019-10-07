#def f(*xs)
def f(*xs,g):
    if len(xs)==0:
        print("空はだめ")
        return

    result = xs[0]
    for i in xs[1:]:
        #if result < i
        if g(result,i):
            result = i
    return result

def my_max(*xs):
    def compare(a,b):
        return a<b
    return f(xs,compare)

def my_min(*xs):
    def compare(a,b):
        return a>b
    return f(xs,compare)

def my_max2(*xs):
    return f(xs,lambda a,b:a<b)

def my_min2(*xs):
    return f(xs,lambda a,b:a>b)

lambda a,b:a*b
lambda a,b:(a*b,a+b)
compare = lambda a,b:a*b

(lambda a,b:a*b)(3,4)
(lambda a,b:(a*b,a+b))(3,4)

print(f(1,5,7))
print(f(1,5,7,-8,1000))
print(f(2))
print(f())

print(f(1,5,7))
print(f(1,5,7,-8,1000))
print(f(2))
print(f())
