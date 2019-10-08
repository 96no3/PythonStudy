class Prime:
    def __init__(self,x=10,*,mode=0):
        """@param x     閾値(default=10)
           @param mode　0＝個数　1＝最大値（default=0）"""
        is_num = lambda x:isinstance(x,int)

        if not is_num(x) or not is_num(mode) or (mode < 0 or mode > 1):
            raise ValueError
        
        self.x = x
        self.mode = mode    
        
    def __str__(self):
        return "prime numbers"
    
    def __iter__(self):
        self.count = 0
        self.num = 1
        return self
    
    def __next__(self):
        if self.mode == 0 and self.count >= self.x:
            raise StopIteration
        
        is_prime = False
        self.num += 1
        while not is_prime:            
            is_prime = True
            for i in range(2,self.num):
                if self.num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                break
            self.num += 1

            if self.mode == 1 and self.num >= self.x:
                raise StopIteration
        self.count += 1
        return self.num

p = Prime(100,mode=1)
print("str:",str(p))
for i in p:
    print(i,end=" ")


