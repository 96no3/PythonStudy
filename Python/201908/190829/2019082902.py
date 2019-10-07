def f():
    print(x)

def g():
    # globalな変数で定義されているｘを再度定義している
    # ＝ この関数内のｘはprintの下にあるのでエラー
    #global x  # globalなｘを参照すればエラーはなくなるが、下のｘはローカルではなくなる
    print(x)
    #x=1   # ローカルな変数を使いたいのであれば、別の変数名にする
    #もしくは関数内関数を定義してreturnで値を返す
    def local_num():
        x=0
        return x
    return local_num()

x=3
f()
x=3
g=g()
print(g)
