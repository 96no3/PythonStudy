class Fibonacci:
    def __init__(self,x=10,*,mode=0):
        """@param x     閾値(default=10)
           @param mode　0＝個数　1＝最大値（default=0）"""
        if not Fibonacci.is_num(x) or not Fibonacci.is_num(mode)\
           or (mode < 0 or mode > 1):
            raise ValueError
        
        self._x = x
        self._mode = mode

    @staticmethod
    def is_num(x):
        return isinstance(x,int)

    @property
    def mode(self):
        return self._mode

    @property
    def threshold(self):
        return self._x

    @mode.setter
    def mode(self,value):
        if not Fibonacci.is_num(value) or (value < 0 or value > 1):
            raise ValueError
        self._mode = value

    @threshold.setter
    def threshold(self,value):
        if not Fibonacci.is_num(value):
            raise ValueError
        self._x = value
        
    def __str__(self):
        return "fibonacci numbers"
    
    def __iter__(self):
        self._count = 0
        self._preResult = 1
        self._result = 1
        return self
    
    def __next__(self):
        if self._mode == 0 and self._count >= self._x:
            raise StopIteration        
        
        if self._count == 0 or self._count == 1:
            self._count += 1
            return self._result
        else:
            result = self._preResult + self._result
            if self._mode == 1 and result >= self._x:
                raise StopIteration
            self._preResult = self._result
            self._result = result
            self._count += 1
            return result                   

fib = Fibonacci()
print("str:",str(fib))
print("mode:",fib.mode,"threshold:",fib.threshold)
for i in fib:
    print(i,end=" ")
fib.mode = 1
fib.threshold = 200
print("\nmode:",fib.mode,"threshold:",fib.threshold)
for i in fib:
    print(i,end=" ")
