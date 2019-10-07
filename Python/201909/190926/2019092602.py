#
# 逆ポーランド記法電卓 再帰版 その4
#
import math

_stack = []

def push(x):
    _stack.append(x)

def pop():
    return _stack.pop()

def clear_stack():
    _stack.clear()

def stack_depth():
    return len(_stack)

def calc(xs):
    print(xs,_stack)
    if not xs:
        return pop()

    operate(xs[0])
    return calc(xs[1:])

def generate(n,f):
    """<高階関数かつクロージャ>
       要素数分スタックからpopして関数を適用しスタックにpushする
       @param n 要素数
       @param f 数式関数オブジェクト
       @return proc 適用処理関数"""
    def proc():
        args = [pop() for _ in range(n)]
        args.reverse()
        push(f(*args))
    return proc

_op_table = ( ("+",2,lambda a,b:a+b),
              ("-",2,lambda a,b:a-b),
              ("*",2,lambda a,b:a*b),
              ("/",2,lambda a,b:a/b),
              ("//",2,lambda a,b:a//b),
              ("**",2,lambda a,b:a**b),
              ("root",1,math.sqrt),
              ("if",3,lambda a,b,c: b if a else c) )

op_dic = dict([(name,generate(n,f)) for name,n,f in _op_table])
del _op_table

def operate(x):
    if isinstance(x,int):
        push(x)
    elif x in op_dic:
        op_dic[x]()
    else:
        raise ValueError(f"unknown operator: {x}")

def execute(s):
    def convert(elem):
        if elem.isdigit():
            return int(elem)
        else:
            return elem

    parsed = s.split(" ")
    elems = [convert(elem) for elem in parsed if elem != ""]
    print("計算結果>",calc(elems))

while True:
    s = input("後置記法の数式を入力してください> ")
    if s.lower() in {"exit","quit","bye"}:
        break
    clear_stack()
    try:
        execute(s)
        if stack_depth() > 0:
            print("スタックに値が残っています！")
    except:
        print("不正な式です!")
