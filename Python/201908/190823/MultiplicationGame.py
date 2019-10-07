from random import randint as rand

def RandPos(posNum):
    return rand(0,posNum-1)

def RandNum(maxNum):
    return rand(1,maxNum)
    
def Make99Question():
    a,b = RandNum(9),RandNum(9)
    c = [a, b, a * b]
    pos = RandPos(len(c)) # マジックナンバーを使わすシーケンスの長さで汎用性向上
    return (c,pos)

repeatNum = int(input("Please input repeat count:"))

count=0
for i in range(repeatNum):
    x,pos = Make99Question()
    print("")
    print(f"x = {x}")
    print(f"pos = {pos}")
    tmp=x[pos]
    x[pos] = "?"
    print(f"{x[0]} x {x[1]} = {x[2]}")
    hand = int(input("? 部分にあてはまる整数を入力してください："))
    if hand == tmp:
        print("正解")
        count += 1
    else:
        print("残念")

print(f"{repeatNum}問中 {count}問正解")
