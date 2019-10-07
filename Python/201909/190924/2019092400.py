# ループを使った足し合わせ
def sum(n):
    result = 0
    for i in range(1,n+1):
        result += i
    return result

# 再帰を使った足し合わせ
def sum2(n):
    if n == 1:
        return 1
    return n + sum2(n-1)

# リスト要素を再帰で足し合わせる処理の例
def sum(xs):
    if not xs:  # xsが空の場合 xs==[]
        return 0
    return xs[0]+sum3(xs[1:])

# 課題ヒント
_stack = []

def push(x):
    _stack.append(x)

def pop():
    return _stack.pop()

def clear_stack():
    _stack.clear()

def stack_depth():
    return len(_stack)

def calc(xs):
    print(xs,_stack)
    if not xs:
        return pop()

    operate(xs[0])
    return calc(xs[1:])
