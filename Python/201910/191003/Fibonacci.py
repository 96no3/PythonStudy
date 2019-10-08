class Fibonacci:
    def __init__(self,x=10,*,mode=0):
        self.x = x
        self.mode = mode

    @staticmethod
    def fib(n):
        if n == 0 or n == 1:
            return 1
        else:
            return Fibonacci.fib(n-1)+Fibonacci.fib(n-2)
        
    def __str__(self):
        return "fibonacci numbers"
    
    def __iter__(self):
        self.count = 0
        return self
    
    def __next__(self):
        if self.count >= self.x:
            raise StopIteration
        result = Fibonacci.fib(self.count)
        self.count += 1
        return result
                   

fib = Fibonacci(20)
print("str:",str(fib))
for i in fib:
    print(i,end=" ")
        
    


