import math

class Stack:
    def __init__(self):
        self._stack = []

    def push(self,x):
        self._stack.append(x)

    def pop(self):
        return self._stack.pop()

    def clear(self):
        self._stack.clear()

    def depth(self):
        return len(self._stack)
        
stack = Stack()
_floating_point = 5

def err():
    raise ValueError

def generate(n,f):
    """<高階関数かつクロージャ>
       要素数分スタックからpopして関数を適用しスタックにpushする
       @param n 要素数
       @param f 数式関数オブジェクト
       @return proc 適用処理関数"""
    def proc():
        args = [float(stack.pop()) for _ in range(n)]
        args.reverse()
        tmp = f(*args)
        stack.push(round(tmp,_floating_point))
    return proc

_op_table = ( ("+",2,lambda a,b:a+b),
              ("-",2,lambda a,b:a-b),
              ("*",2,lambda a,b:a*b),
              ("/",2,lambda a,b:a/b),
              ("%",2,lambda a,b:a%b),
              ("//",2,lambda a,b:a//b),
              ("**",2,lambda a,b:a**b),
              ("root",1,math.sqrt),
              ("log",1,math.log),
              ("sin",1,lambda a:math.sin(math.radians(a))),
              ("cos",1,lambda a:math.con(math.radians(a))),
              ("tan",1,lambda a:math.tan(math.radians(a))),
              ("if",3,lambda a,b,c: b if a else c) )

op_dic = dict([(name,generate(n,f)) for name,n,f in _op_table])
del _op_table

def calc(xs):
    print(xs,stack._stack)
    if not xs:        
        if stack.depth() == 1:
            return stack.pop()
        else:
            print("スタックに値が残っています！")
            err()
            
    operate(xs[0])
    return calc(xs[1:])

def operate(x):    
    if x in op_dic:
        op_dic[x]()
    elif validate_num(x):
        stack.push(x)
    else:
        raise ValueError(f"unknown operator: {x}")

def input_num_expression():
    """入力を求める関数"""
    return input("後置記法で数式を入力してください:")

def get_num_expression(function):
    """＜高階関数＞入力を求める関数の値を判断する関数
       @param function  入力処理を行う関数
       @return tmp_list 認識可能なlist"""
    while True:
        s = function()        
        if s.lower() in {"exit","quit","bye"}:
            break
        try:
            if s == "":
                err()            
            tmp_list = s.split(" ")            
            tmp_list = list(filter(lambda a:a is not "", tmp_list))
            validate_element(tmp_list)
            return tmp_list
        except:
            print(f"「{s}」は無効な入力値です\n正しい入力値をお願いします")
    return "exit"

def validate_element(xs):
    """<検査関数>有効な要素かどうか検査する関数
       @param xs 入力値の各要素リスト
       @return  各要素リスト"""    
    if xs == []:
        return xs    
    elif xs[0] in op_dic:
        validate_element(xs[1:])
    elif validate_num(xs[0]):
        validate_element(xs[1:])
    else:
        print("無効な入力エラー")
        err()

def validate_num(s):
    """<検査関数>有効な数値かどうか検査する関数
       @param s 文字列
       @return  有効な数値の文字列"""
    if s[0] == "-":
        validate_num(s[1:])
    elif s[0] == "+":
        validate_num(s[1:])
    elif s.count(".") == 1:
        [a,b] = s.split(".")
        if not a.isdigit() or not b.isdigit():
            err()
        return True
    elif not s.isdigit():
        err()
    return True

def test_exec():
    while True:
        num_expression = get_num_expression(input_num_expression)
        if num_expression == "exit":
            return False
        try:
            print("\n計算結果>",calc(num_expression),"\n")
        except:
            print(f"「{num_expression}」は計算不可能な式です")
            print("正しい入力値をお願いします")
            stack.clear()
            
def test():
    while test_exec():
        pass
    print("end")

# 実行部分
test()
