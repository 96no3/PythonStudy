# whileでの九九
x=0
while x<9:
    y=1    
    x+=1
    print(f"****{x}の段****")
    while y<10:
        print(f"{x}x{y} = {x*y}")
        y+=1

def SpeedTest(n):
    print("start")
    for i in range(n):
        pass
    print("done")

# iteratorの汎用性
list(range(1,100,5))
tuple(range(1,100,5))
a=list(range(10))
tuple(a)
