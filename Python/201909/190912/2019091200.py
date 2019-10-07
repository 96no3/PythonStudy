# 素数を返すイテレータ
def genPrime(maxNum):
    num=2
    while (num<=maxNum):
        is_prime = True
        for i in range(2,num):
            if(num % i) == 0:
                is_prime = False
                break
        if(is_prime):
            yield num
        num += 1

it = genPrime(50)
for i in it:
    print(i,end=",")
