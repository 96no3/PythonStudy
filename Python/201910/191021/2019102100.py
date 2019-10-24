class C:
    # クラス変数
    x=0
    def __init__(self):
        # インスタンス変数
        self.b=0

print(C.x)
a=C()
b=C()
print(a.x)
print(b.x)

# このようにインスタンスからクラス変数を変更するとインスタンス扱いになる
a.x="hello"
print(C.x)
print(a.x)
print(b.x)

class A:
    x=0

    def __del__(self):
        print("デストラクタ")

class B(A):
    def __init__(self):
        self.parent_x=super().x

# インスタンス生成時にコンストラクタで初期化されるので、値は保持されない
print(B().x)
print(A().x)
B().x=10
print(B().x)
print(A().x)
B().parent_x=10
print(B().x)
print(A().x)
print(B().parent_x)

# クラスオブジェクトからクラス変数を書き換え
A.x=100
print(B().x)
print(A().x)
print(B().parent_x)

# クラスオブジェクトを保持してインスタンス変数を作成すると、
#そのオブジェクトがあればインスタンス変数の値が保持される
a=A()
print(a.x)
a.x=10
print(a.x)

# インスタンスの破棄
del a
