class Queue:
    def __init__(self):
        self._queue = []

    def put(self,x):
        self._queue.append(x)

    def get(self):
        try:
            tmp = self._queue[0]
            del self._queue[0]
            return tmp
        except IndexError:
            print("キューが空です\n")

    def clear(self):
        self._queue.clear()

    def depth(self):
        return len(self._queue)
