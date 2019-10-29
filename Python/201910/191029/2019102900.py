# クラスの継承
class A:
    def name(self):
        return "A"

class B(A):
    pass

b=B()
b.name()
B is A
isinstance(a,A)
isinstance(b,A)
isinstance(a,B)
isinstance(b,B)

class C:
    def __init__(self):
        print("init C")

class D(C):
    def __init__(self):
        print("init D")

C()
D() # このままでは継承元のCのコンストラクタがオーバーライドされる

class D(C):
    def __init__(self):
        #C.__init__(self)
        super().__init__():
        print("init D")

# 全てのデータ型が継承しているもの＝object
isinstance(None,object)
isinstance("",object)
