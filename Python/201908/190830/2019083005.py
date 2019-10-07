def get_int(function):
    """＜高階関数＞入力を求める関数の値を判断する関数
       @param function 入力処理を行う関数
       @return s 認識可能なint数"""
    while True:
        s = function()        
        if s.lower() == "exit":
            break
        if s.isdigit():
            n=int(s)
            if n<=1 or n > 16:
                print(f"「{n}」は2~16の数ではありません\n正しい入力値をお願いします")            
            else:
                return s
        else:
            print(f"「{s}」は正の数値ではありません\n正しい入力値をお願いします")
    return "exit"

def valid(base,base_num):
    """＜検査関数＞入力値が正しいかどうか判定する関数"""    
    if int(base) < 10:
        for i in base_num:
            if not("0" <= i.lower() <= str(base-1)):
                return False
        return True
    
    for i in base_num:
        if not("0" <= i.lower() <= "9" or "a"<= i.lower() <= "f"):
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
        #elif not base_num.isdigit():
        #    print(f"「{base_num}」は数値ではありません\n正しい入力値をお願いします")
        elif not valid(base,base_num):
            print(f"「{base_num}」は{base}進数の数ではありません")
            print("正しい入力値をお願いします")
        else:
            return base_num        

def input_base():
    """入力を求める関数"""
    return input("2~16の範囲で基数を入力してください:")

def input_num(base):
    """入力を求める関数"""
    return input(f"{base} 進数を入力してください:")

def convert(src,*,base=2):
    n_result=0
    for i,x in enumerate(reversed(src)):
        if not x.isdigit():
            dict16 = {"a":10,"b":11,"c":12,"d":13,"e":14,"f":15}
            print(f"Debug:convert「{x}」＝「{dict16[x]}」")
            x = dict16[x]
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
