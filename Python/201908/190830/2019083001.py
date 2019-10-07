def valid(base,src):
    """＜検査関数＞入力値が正しいかどうか判定する関数"""
    
    if len(src) == 0 or base==1 or base>10:
        return False    
    
    # strで判定する場合、２桁以上のbaseが渡されると判定できない
    for i in src:
        #if not("0" <= i < str(base)):
        # 10進数間での対応なら以下の方法で可能だが、1進数には未対応
        if not("0" <= i <= str(base-1)):
            return False
    return True

def input_num():
    tmp = input("基数を入力してください:")
    if tmp.isdigit() and 1<int(tmp)<=10:
        return int(tmp)

def test_exec():
    # 入力エラーをなくす
    #base = int(input("基数を入力してください:"))
    #base = input("基数を入力してください:")
    #if not (base.isdigit() and 0<=int(base)<=9):
    #    return False
    #base = int(base)

    while True:
        base = input_num()
        # if base is not Noneならばと同様 
        if base:            
            break
    
    src = input(f"{base} 進数を入力してください:")
    if src.lower() == "exit":
        return False
    elif not valid(base,src):
        print(f"不正な{base}進数:",src)
        return False
    print("求める10進数は:",convert(src,base=base),"\n")
    return True

def convert(src,*,base=2):
    n_result=0
    for i,x in enumerate(reversed(src)):
        n_result += int(x)*base**i
        print(f"Debug i:{i} x:{x} {base}**{i}={base**i}  result:{n_result}")     
    return n_result    

def test():
    while test_exec():
        pass
    print("end")

#実行部分
test()