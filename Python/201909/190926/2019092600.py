#
# 逆ポーランド記法電卓 再帰版 その2
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

op_dic = { "+":(2,lambda a,b:a+b),
           "-":(2,lambda a,b:a-b),
           "*":(2,lambda a,b:a*b),
           "/":(2,lambda a,b:a/b),
           "//":(2,lambda a,b:a//b),
           "**":(2,lambda a,b:a**b),
           "root":(1,math.sqrt) }           

def operate(x):
    if isinstance(x,int):
        push(x)
    elif x in op_dic:
        n_args,f = op_dic[x]
        if n_args == 2:
            b = pop()
            a = pop()
            push(f(a,b))
        else: # n_args == 1
            push(f(pop()))
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
