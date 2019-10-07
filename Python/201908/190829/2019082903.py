def get_binary_list(function):
    """＜高階関数＞入力を求める関数の値を判断する関数
       @param function 入力処理を行う関数
       @return bits 正しい入力値の2進数リスト"""
    while True:
        bits = function()
        if bits.lower() == "exit":
            break
        
        n=len(bits)
        if n==0:
            print(f"「{bits}」は空です\n正しい入力値をお願いします")
        elif bits.count("0")+bits.count("1") != n:
            print(f"「{bits}」は0,1の数ではありません\n正しい入力値をお願いします")
        else:
            return bits
    return "exit"

def input_num():
    """入力を求める関数"""
    return input("Please input Binary number:")

def convert(bits):
    n_decimal=0
    for i,x in enumerate(reversed(bits)):
        n_decimal += int(x)*2**i
        print("Debug","i:",i,"x:",x,"result:",n_decimal)     
    return n_decimal    

def test_exec():
    bits = get_binary_list(input_num)     
    if bits.isdigit():
        print("Decimal number:",convert(bits),"\n")
        return True
    else:
        return False

def test():
    while test_exec():
        pass
    print("end")

# 実行部分
#bs = input("Please input Binary number:")
#rbs=list(reversed(bs))
#n_decimal=0

#for i in range(len(rbs)):
#    n_decimal += int(rbs[i])*2**i

#print("Decimal number:",n_decimal)

test()
