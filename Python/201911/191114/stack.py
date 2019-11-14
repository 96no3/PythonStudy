class Stack:
    def __init__(self):
        self._stack = []

    def push(self,x):
        self._stack.append(x)

    def pop(self):
        try:
            tmp = self._stack.pop()
            return tmp
        except IndexError:
            print("スタックが空です\n")

    def clear(self):
        self._stack.clear()

    def depth(self):
        return len(self._stack)
