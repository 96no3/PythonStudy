_operators=["+", "-", "*","/"]
_stack=[]
_necessary_num = 5

def push(x):
    _stack.append(x)

def pop():
    return _stack.pop()

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
            elif len(s) < _necessary_num:
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
    elif xs[0].isdigit():
        validate_element(xs[1:])
    elif _operators.count(xs[0]) < 1:
        err()
    elif _operators.count(xs[0]) == 1:
        validate_element(xs[1:])
    else:
        print("その他、無効な入力エラー")
        err()

def calculation(num_expression_list):
    print("Debug:",num_expression_list,_stack)
    if num_expression_list == []:
        if len(_stack) == 1:
            print("実行結果",_stack)
            _stack.clear()
            return True
        else:
            err()
    elif num_expression_list[0].isdigit():
        push(num_expression_list[0])
        calculation(num_expression_list[1:])
    else:
        tmp_num1 = pop()
        tmp_num2 = pop()
        push(str(eval(tmp_num2+num_expression_list[0]+tmp_num1)))
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
            
def test():
    while test_exec():
        pass
    print("end")

# 実行部分
test()
