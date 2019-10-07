# f"{}"フォーマット文字
def Add(num1,num2):
    print(f"{num1} + {num2} = {num1+num2}")

x=float(input("number x:"))
y=float(input("number y:"))
Add(x,y)

m=str(input("string1:"))
n=str(input("string2:"))
Add(m,n)

# ListとTuple
a=["a",1,0] # List
print(a+a)
a+=[10,1]
print(a)

b=(2,"b",3) # Tuple
print(b[1])
b+=(7,9)
print(b)

print("List a")
for x in a:
    print(x)

print("Tuple b")
for x in b:
    print(x)

# range()でのfor文
for i in range(10):
    print(i*i)

for i in range(2,10):
    for j in range(3):
        print(f"{i}x{j} = {i*j}")    

for i in range(2,10,3):
    print(i)

for i in range(1,10):
    print(f"****{i}の段****")
    for j in range(1,10):
        print(f"{i}x{j} = {i*j}")

# whileでの九九
x=0
while x<9:
    y=1    
    x+=1
    print(f"****{x}の段****")
    while y<10:
        print(f"{x}x{y} = {x*y}")
        y+=1
    
# inについて
0 in range(2)
2 in [0,2,5]
