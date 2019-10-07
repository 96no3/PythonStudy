x=[[-1,2,3],[1,0,-2]]
list(map(lambda a: list(map(lambda e: 0 if e <= 0 else e,a)),x))

list(map(lambda a: len(list(filter(lambda e:e>=1,a))),x))
sum(map(lambda a: len(list(filter(lambda e:e>=1,a))),x))

# 二次元配列
import numpy as np
np.array(x)

class A:
    pass

a=A()
isinstance(a,A)
isinstance(a,int)

a.x=1
a.x += 10
a.b=10

class Person:
    name = None
    age = None
    addr = None

Person().name
a = Person()
a,name = "James"
b = Person()
isinstance(a,A)
isinstance(a,Person)

class B:
    #name = "default"
    def __init__(self,name="default"):
        self.name = name
        print("initialized!",self.name)
        
    def set_name(self,name):
        self.name = name
        
    def get_name(self):
        return f"My name is {self.name}"

B()
b=B("James")
b.get_name()

# 非オブジェクト指向
_stack = []

def push(x):
    _stack.append(x)

def pop():
    return _stack.pop()

def clear_stack():
    _stack.clear()

def stack_depth():
    return len(_stack)

# オブジェクト指向的アプローチ
class Stack:
    def __init__(self):
        self._stack = []

    def push(self,x):
        self._stack.append(x)

    def pop(self):
        return self._stack.pop()

    def clear(self):
        self._stack.clear()

    def depth(self):
        return len(self._stack)

stk = Stack()
stk.push(x)
Stack.push(stk,x)

# 間違った設計のオブジェクト指向的アプローチ
class WrongStack:
    _stack = [] # このリストがすべてのインスタンスで共有されてしまう

    def push(self,x):
        self._stack.append(x)

    def pop(self):
        return self._stack.pop()

    def clear(self):
        self._stack.clear()

    def depth(self):
        return len(self._stack)

def test(stk1,stk2):
    stk1.push("stk1-1")
    stk2.push("stk2-1")
    stk1.push("stk1-2")
    stk1.push("stk1-3")
    stk2.push("stk2-2")

    print("stk1.depth() is",stk1.depth())
    print("stk2.depth() is",stk2.depth())
    print("stk1.pop() --->",stk1.pop())
    print("stk1.pop() --->",stk1.pop())
    print("stk1.pop() --->",stk1.pop())
    print("stk2.pop() --->",stk2.pop())
    print("stk2.pop() --->",stk2.pop())

test(Stack(),Stack())
test(WrongStack(),WrongStack())
