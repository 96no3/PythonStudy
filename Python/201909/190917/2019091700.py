# filter関数
list(filter(lambda x:x%2==1,range(100)))

# リスト内包表記
[x**2 for x in range(100) if x%2 == 1]

# 再帰関数
def my_sum(n):
    if n == 1:
        return 1
    else:
        return n + my_sum(n-1)

my_sum(10)

def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

fac(10)

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-2)+fib(n-1)

fib(5)
[fib(i) for i in range(20)]

# joinメソッド
"".join(["ab","cd","e"])
",".join(["ab","cd","e"])
" ".join(["ab","cd","e"])

# 有効な数値かどうか検査する関数
def validate_num(s):
    if s == "":
        raise ValueError
    elif s[0] == "-":
        validate_num(s[1:])
    elif s.count(".") == 1:
        [a,b] = s.split(".")
        if not (a or b) or (a and not a.isdigit()) or (b and not b.isdigit()):
            raise ValueError
        elif not s.isdigit():
            raise ValueError

def test():
    while True:
        s = input("number: ")
        validate_num(s)
