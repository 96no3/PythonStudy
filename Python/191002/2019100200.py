class Stack:
    def __init__(self):
        self._stack = []

    def push(self,x):
        self._stack.append(x)

    def pop(self):
        return self._stack.pop()

class CompleteStack(Stack):
    def __init__(self):
        super().__init__()
        #Stack.__init__(self)

    def clear(self):
        self._stack.clear()

    def depth(self):
        return len(self._stack)

class ExStack(CompleteStack):
    def __init__(self):
        super().__init__()

    def push(self,x,*xs):
        super().push(x)
        for i in xs:
            super().push(i)

    def pop(self,n=1):
        for _ in range(n):
            result = super().pop()
        return result

es = ExStack()
es.push(1,2,3)
print("stack:",es._stack)
print("depth:",es.depth())

print("pop(2):",es.pop(2))
print("depth:",es.depth())

es.clear()
print("depth:",es.depth())
