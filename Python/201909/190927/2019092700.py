"a,b,c".split(",")
str.split("a,b,c",",")

rule = [(3,2),(4,5),(3,1)]
def test(xs,w):
    if xs:
        a,b = xs[0]
        print(w+a,w-b)
        test(xs[1:],w+a)
        test(xs[1:],w-b)

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


