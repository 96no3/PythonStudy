import math

_operators=["+", "-", "*","/","//","%","**"]
_tri_func = {"sin":math.sin,"cos":math.cos,"tan":math.tan}
_math_func = {"log":math.log,"r":math.sqrt}

_necessary_num = 1
_floating_point = 5

class Stack:
    def __init__(self):
        self._stack = []

    def push(self,x):
        self._stack.append(x)

    def pop(self):
        return self._stack.pop()

    def clear(self):
        self._stack.clear()
        
stack = Stack()
infix = Stack()

def err():
    raise ValueError

def input_num_expression():
    """入力を求める関数"""
    return input("後置記法で数式を入力してください:")

def get_num_expression(function):
    """＜高階関数＞入力を求める関数の値を判断する関数
       @param function  入力処理を行う関数
       @return tmp_list 認識可能なlist"""
    while True:
        s = function()        
        if s.lower() == "exit":
            break
        try:
            if s == "":
                err()            
            tmp_list = s.split(" ")
            tmp_list = list(filter(lambda a:a is not "", tmp_list))
            if len(tmp_list) < _necessary_num:
                err()
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
    elif _operators.count(xs[0]) == 1:
        validate_element(xs[1:])
    elif xs[0] in _tri_func:
        validate_element(xs[1:])
    elif xs[0] in _math_func:
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

def calculation(num_expression_list):
    """後置記法（逆ポーランド記法）の計算関数
       @param num_expression_list 計算式のリスト
       @retval True       計算終了結果表示
               ErrorValue 計算不可能な式"""    
    print("Debug:",num_expression_list,stack._stack)
    if num_expression_list == []:
        if len(stack._stack) == 1:
            print("\n実行結果",stack.pop())
            print("中置記法での式:",infix.pop(),"\n")
            return True
        else:
            err()
    elif _operators.count(num_expression_list[0]) == 1:
        tmp_num1 = stack.pop()
        tmp_num2 = stack.pop()
        infix_num1 = infix.pop()
        infix_num2 = infix.pop()
        infix.push("("+infix_num2+num_expression_list[0]+infix_num1+")")
        result = eval(tmp_num2+num_expression_list[0]+tmp_num1)
        stack.push(str(round(result,_floating_point)))
        calculation(num_expression_list[1:])
    elif num_expression_list[0] in _tri_func:
        tmp_num = eval(stack.pop())
        infix_num = infix.pop()
        infix.push(num_expression_list[0]+"("+infix_num+")")
        result = _tri_func[num_expression_list[0]](math.radians(tmp_num))
        stack.push(str(round(result,_floating_point)))
        calculation(num_expression_list[1:])
    elif num_expression_list[0] in _math_func:
        tmp_num = eval(stack.pop())
        infix_num = infix.pop()
        infix.push(num_expression_list[0]+"("+infix_num+")")
        result = _math_func[num_expression_list[0]](tmp_num)
        stack.push(str(round(result,_floating_point)))
        calculation(num_expression_list[1:])
    elif validate_num(num_expression_list[0]):
        stack.push(num_expression_list[0])
        infix.push(num_expression_list[0])
        calculation(num_expression_list[1:])        

def test_exec():
    while True:
        num_expression = get_num_expression(input_num_expression)
        if num_expression == "exit":
            return False
        try:
            calculation(num_expression)
        except:
            print(f"「{num_expression}」は計算不可能な式です")
            print("正しい入力値をお願いします")
            stack.clear()
            infix.clear()
            
def test():
    while test_exec():
        pass
    print("end")

# 実行部分
test()
