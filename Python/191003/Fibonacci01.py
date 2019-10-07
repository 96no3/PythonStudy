class Fibonacci:
    def __init__(self,x=10,*,mode=0):
        """@param x     閾値(default=10)
           @param mode　0＝個数　1＝最大値（default=0）"""
        is_num = lambda x:isinstance(x,int)

        if not is_num(x) or not is_num(mode) or (mode < 0 or mode > 1):
            raise ValueError
        
        self.x = x
        self.mode = mode
        
    def __str__(self):
        return "fibonacci numbers"
    
    def __iter__(self):
        self.count = 0
        self.preResult = 1
        self.result = 1
        return self
    
    def __next__(self):
        if self.mode == 0 and self.count >= self.x:
            raise StopIteration        
        
        if self.count == 0 or self.count == 1:
            self.count += 1
            return self.result
        else:
            result = self.preResult + self.result
            if self.mode == 1 and result >= self.x:
                raise StopIteration
            self.preResult = self.result
            self.result = result
            self.count += 1
            return result                   

fib = Fibonacci(100,mode=1)
print("str:",str(fib))
for i in fib:
    print(i,end=" ")
        
    


