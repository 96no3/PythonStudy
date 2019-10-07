def input_type():
    """入力を求める関数"""
    message1 = "シーザー暗号化する場合は「0」\n"
    message2 = "シーザー暗号を復号化する場合は「1」を入力してください:"
    return input(message1+message2)

def get_type(function):
    """＜高階関数＞入力を求める関数の値を判断する関数
       @param function 入力処理を行う関数
       @retval 0 シーザー暗号化する場合の数字の文字列
       @retval 1 シーザー暗号を復号化する場合の数字の文字列
       @retval "exit" 終了処理用文字列"""
    while True:
        num = function()
        if len(num)==0:
            print(f"「{num}」は空です\n正しい入力値をお願いします")
        elif num.lower() == "exit":
            break        
        elif num.isdigit():
            _n = int(num)
            if _n==0 or _n==1:
                return _n            
        else:
            print(f"「{num}」は「0」または「1」の整数ではありません")
            print("正しい入力値をお願いします")            
    return "exit"


def input_num():
    """入力を求める関数"""
    return input("シーザー暗号に必要な「数」を入力してください:")

def get_num(function):
    """＜高階関数＞入力を求める関数の値を判断する関数
       @param function 入力処理を行う関数
       @return num 利用可能な数字の文字列"""
    while True:
        num = function()
        if len(num)==0:
            print(f"「{num}」は空です\n正しい入力値をお願いします")
        elif not num.isdigit():
            print(f"「{num}」は正の整数ではありません")
            print("正しい入力値をお願いします")
        else:
            return num

def input_ascii_string():
    """入力を求める関数"""        
    return input("シーザー暗号で変換したい「文字列」を入力してください:")

def get_ascii_string(function):
    """＜高階関数＞入力を求める関数の値を判断する関数
       @param function 入力処理を行う関数
       @return s 認識可能なstring"""
    while True:
        s = function()
        if not s.isascii():
            print(f"「{s}」は暗号化可能な文字ではありません")
            print("正しい入力値をお願いします")
        else:
            return s

def make_byte_string(string):
    """str型文字列をバイト文字列に変換する関数
       @param string str型文字列
       @return       バイト文字列"""
    return str(x).encode()

def make_to_string(byte_string):
    """バイト文字をstr型に変換する関数
       @param byte_string バイト文字列
       @return            str型の文字列"""
    if isinstance(byte_string,bytes):
        return byte_string.decode()        

def caesar_char(char_string,add_num):
    """文字をシーザー暗号化したアスキーコードの数を返す関数
       @param char_string 変換したいstr型の1文字
       @param add_num     シーザー暗号化で基のアスキーコードに加える数
       @return  シーザー暗号化したアスキーコードの数"""
    if "a" <= char_string <= "z":
        alpha_base = ord("a")
    elif "A" <= char_string <= "Z":
        alpha_base = ord("A")
    else:
        print(f"{char_string}")

    alpha_code = ord(char_string) - alpha_base
    return (alpha_code + add_num) % 26 + alpha_base

def caesar_num(num_string,add_num):
    """数をシーザー暗号化したアスキーコードの数を返す関数
       @param num_string 変換したいstr型の1数
       @param add_num     シーザー暗号化で基のアスキーコードに加える数
       @return  シーザー暗号化したアスキーコードの数"""
    if "0" <= num_string <= "9":
        alpha_base = ord("0")
    else:
        print(f"{num_string}")
    alpha_code = ord(num_string) - alpha_base
    return (alpha_code + add_num) % 10 + alpha_base

def check_num(num,adjust_num):
    """数が負の場合、調整する数を用いて正の数を返す関数
       @param num        確認したい数
       @param adjust_num シーザー暗号化で基のアスキーコードに加える数
       @return  num      シーザー暗号の復号に必要な数"""
    while True:
        print(f"Debug:before「{num}」")
        if num<0:
            num += adjust_num
            print(f"Debug:after「{num}」")
        else:
            return num

def de_caesar_char(caesar_string,take_num):
    """シーザー暗号化した文字を復号化したアスキーコードの数を返す関数
       @param caesar_string 変換したいstr型の1文字
       @param take_num      シーザー暗号を復号する時にアスキーコードから戻す数
       @return              シーザー暗号を復号化したアスキーコードの数"""
    if "a" <= caesar_string <= "z":
        alpha_base = ord("a")
    elif "A" <= caesar_string <= "Z":
        alpha_base = ord("A")
    else:
        print(f"{caesar_string}")

    alpha_code = ord(caesar_string) - alpha_base
    tmp = check_num((alpha_code - take_num),26)
    return tmp % 26 + alpha_base

def de_caesar_num(caesar_num_string,take_num):
    """シーザー暗号化した数を復号化したアスキーコードの数を返す関数
       @param caesar_num_string 変換したいstr型の1数
       @param take_num          シーザー暗号を復号する時にアスキーコードから戻す数
       @return                  シーザー暗号を復号化したアスキーコードの数"""
    if "0" <= caesar_num_string <= "9":
        alpha_base = ord("0")
    else:
        print(f"{caesar_num_string}")
    alpha_code = ord(caesar_num_string) - alpha_base
    tmp = check_num((alpha_code - take_num),10)
    return tmp % 10 + alpha_base

def test_exec():
    type_num = get_type(input_type)
    if type_num == "exit":        
        return False
    
    num = get_num(input_num)    
    _num = int(num)
    
    string = get_ascii_string(input_ascii_string)
    string_list = list(string)
    print(f"Debug: string_list = {string_list}")
    for i in range(len(string_list)):
        if string_list[i].isdigit():
            if type_num==0:
                string_list[i] = caesar_num(string_list[i],_num)
            else:
                string_list[i] = de_caesar_num(string_list[i],_num)            
        else:
            if type_num==0:
                string_list[i] = caesar_char(string_list[i],_num)
            else:
                string_list[i] = de_caesar_char(string_list[i],_num)
            
    print(f"Debug: convert string_list = {string_list}")
    byte_string = bytes(string_list)
    if type_num==0:
        print("シーザー暗号は:",make_to_string(byte_string),"\n")
    else:
        print("シーザー暗号を復号化した文字列は:",make_to_string(byte_string),"\n")
    
    return True

def test():
    while test_exec():
        pass
    print("end")

# 実行部分
test()

            