def test1():
    x = "original x"
    result = []
    # 関数内のｘを書き換えてしまう副作用のある記述
    # ブロックスコープはpythonではない
    for x in range(10):
        result.append(x*x)
    print(result)
    return x

print(test1())

def test2():
    x="original x"
    # リスト内包内のｘはローカル扱いになり、非破壊的扱い
    print([x*x for x in range(10)])
    return x

print(test2())

def test3():
    print([x*x for x in range(10)])
    # リスト内包内はブロックスコープのような扱いになり、ｘを得ることはできない
    return x # エラー

print(test3())
