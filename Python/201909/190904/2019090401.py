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

def valid(base,base_num):
    """＜検査関数＞入力値が正しいかどうか判定する関数"""
    # dictionaryを作成し、その中に入力値があるかチェックが必要
    if int(base) < 10:
        for i in base_num:
            if not("0" <= i.lower() <= str(base-1)):
                return False
        return True
    
    for i in base_num:
        if not("0" <= i.lower() <= "9" or "a"<= i.lower() <= "z"):
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

def input_base():
    """入力を求める関数"""
    return input("2~36の範囲で基数を入力してください:")

def input_num(base):
    """入力を求める関数"""
    return input(f"{base} 進数を入力してください:")

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

def convert(src,*,base=2):
    n_result=0
    for i,x in enumerate(reversed(src)):
        if not x.isdigit():
            """dict36 = {"a":10,"b":11,"c":12,"d":13,"e":14,"f":15\
                      ,"g":16,"h":17,"i":18,"j":19\
                      ,"k":20,"l":21,"m":22,"n":23,"o":24,"p":25\
                      ,"q":26,"r":27,"s":28,"t":29\
                      ,"u":30,"v":31,"w":32,"x":33,"y":34,"z":35}"""
            dict36 = make_char_dict36("a",10,26)
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
