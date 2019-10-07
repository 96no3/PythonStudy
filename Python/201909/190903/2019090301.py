# 論理演算子の確認用
def test(x,i):
    print(x,"is provided","id=",i)
    return x

print(test(True,1) and test(True,2),"\n")
print(test(False,1) and test(True,2),"\n")
print(test(True,1) or test(True,2),"\n")
print(test(False,1) or test(True,2),"\n")
print(test(True,1) or test(False,2),"\n")

def caesar_char(c,m):
    if "a" <= c <= "z":
        alpha_base = ord("a")
    elif "A" <= c <= "Z":
        alpha_base = ord("A")
    else:
        print(f"{c}")

    alpha_code = ord(c) - alpha_base
    return (alpha_code + m) % 26 + alpha_base

print(bytes([caesar_char("a",3)]))
print(bytes([caesar_char("z",3)]))
print(bytes([caesar_char("D",3)]))
print(bytes([caesar_char("X",3)]))
