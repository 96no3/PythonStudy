class Prime:
    def __init__(self,x=100,*,mode=0):
        self.x = x
        self.mode = mode    
        
    def __str__(self):
        return "prime numbers"
    
    def __iter__(self):
        self.num = 1
        return self
    
    def __next__(self):
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

            if self.num >= self.x:
                raise StopIteration
        return self.num

p = Prime(10000)
print("str:",str(p))
for i in p:
    print(i,end=" ")


