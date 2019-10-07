def input_num():
    """入力を求める関数"""
    return input("数を入力してください：")

def get_num(function):
    """＜高階関数＞入力を求める関数の値を判断する関数
       @param function 入力処理を行う関数
       @return         正しい入力値の数値"""
    while True:
        s = function()
        try:
            validate_num(s)
            return eval(s)
        except:
            print(f"「{s}」は無効な入力値です\n正しい入力値をお願いします")            
 
def validate_num(s):
    """<検査関数>有効な数値かどうか検査する関数
       @param s 文字列
       @return  有効な数値の文字列"""
    def err():
        raise ValueError
    
    if s == "":
        err()
    elif s[0] == "-":
        validate_num(s[1:])
    elif s[0] == "+":
        validate_num(s[1:])
    elif s.count(".") == 1:
        [a,b] = s.split(".")
        if not a.isdigit() or not b.isdigit():
            err()
        return s
    elif not s.isdigit():
        err()
    return s

print(get_num(input_num))
