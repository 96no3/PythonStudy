def input_base():
    """入力を求める関数"""
    return input("2~36の範囲で基数を入力してください:")

def get_int(function):
    """＜高階関数＞入力を求める関数の値を判断する関数
       @param function 入力処理を行う関数
       @return s 認識可能なstring"""
    while True:
        s = function()        
        if s.lower() == "exit":
            break
        if s.isdigit():
            n=int(s)
            if n<=1 or n > 36:
                print(f"「{n}」は2~36の数ではありません\n正しい入力値をお願いします")            
            else:
                return s
        else:
            print(f"「{s}」は正の数値ではありません\n正しい入力値をお願いします")
    return "exit"

def make_char_list(char,count):
    """基となるchar文字列から連続した文字をリスト化する関数
       @param char  基にするchar文字列
       @param count 作成したいリストの要素数
       @return _char_list 文字列リスト"""
    _char_list = []
    _base = ord(char.lower())
    for i in range(count):
        _char_list.append(chr(_base))
        _base += 1
    return _char_list

def make_num_list(num,count):
    """基となるnum文字列から連続した数をリスト化する関数
       @param num 基にするchar文字列
       @param count 作成したいリストの要素数
       @return _num_list num文字列リスト"""    
    _num_list = []
    _base = ord(str(num).lower())
    for i in range(count):
        _num_list.append(chr(_base))
        _base += 1
    return _num_list

def make_char_dict36(key_char,value_num,count):
    """36進数に対応するdicionaryにする関数
       @param key_char キーとする文字列
       @param base 　　値とする数
       @return base_num 正しい入力値のn進数リスト"""    
    _dictionary = {}
    _key_base = ord(key_char.lower())
    _value_base = int(value_num)
    for i in range(count):
        _dictionary[chr(_key_base)]=_value_base
        _key_base += 1
        _value_base += 1
    return _dictionary

def input_num(base):
    """入力を求める関数"""
    return input(f"{base} 進数を入力してください:")

def valid(base,base_num):
    """＜検査関数＞入力値が正しいかどうか判定する関数"""
    # dictionaryを作成し、その中に入力値があるかチェックが必要
    if int(base) <= 10:
        for i in base_num:
            if not("0" <= i.lower() <= str(base-1)):
                return False
        return True

    _char=make_char_list("a",int(base)-10)
    _num=make_num_list("0",10)
    
    for i in base_num:
        if not("0" <= i.lower() <= "9" or "a"<= i.lower() <= "z"):
            return False
        elif not(i.lower() in _char or i.lower() in _num):
            return False
    return True    

def get_base_num_list(function,base):
    """＜高階関数＞入力を求める関数の値を判断する関数
       @param function 入力処理を行う関数
       @param base 　　基数n
       @return base_num 正しい入力値のn進数リスト"""
    while True:
        base_num = function(base)
        
        if len(base_num)==0:
            print(f"「{base_num}」は空です\n正しい入力値をお願いします")
        elif not valid(base,base_num):
            print(f"「{base_num}」は{base}進数の数ではありません")
            print("正しい入力値をお願いします")
        else:
            return base_num
        
def convert(src,*,base=2):
    n_result=0
    for i,x in enumerate(reversed(src)):
        if not x.isdigit():
            dict36 = make_char_dict36("a",10,base-10)
            print(f"Debug:convert「{x}」＝「{dict36[x.lower()]}」")
            x = dict36[x.lower()]
        n_result += int(x)*base**i
        print(f"Debug i:{i} x:{x} {base}**{i}={base**i}  result:{n_result}")     
    return n_result  

def test_exec():
    base = get_int(input_base)     
    if base.isdigit():
        base=int(base)
        base_num = get_base_num_list(input_num,base)
        print("求める10進数は:",convert(base_num,base=base),"\n")
        return True
    else:
        return False
    
def test():
    while test_exec():
        pass
    print("end")

# 実行部分
test()
