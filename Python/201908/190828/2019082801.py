def f(x):
    def g():
        nonlocal x   # nonlocalで修飾するとxは上の階層のxを参照する
        x= "abc"
        print("x=",x)
    def h():
        global x
        z = x
        print("z=",z)
    x=x+1
    print("x=",x)
    h()
    g()
    print("x=",x)
    return g

x=3
z=f(x)
print("x=",x)
print("z=",z)
z()
