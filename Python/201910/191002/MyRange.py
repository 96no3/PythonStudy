class MyRange:
    def __init__(self,*xs):
        n = len(xs)
        if n == 0 or n > 3:
            raise SyntaxError
        elif n == 1:
            if xs[0] <= 0:
                raise SyntaxError
            else:
                first = 0
                end = xs[0]
                step = 1            
        elif n == 2:
            if xs[0] >= xs[1]:
                raise SyntaxError
            else:
                first = xs[0]
                end = xs[1]
                step = 1
        elif n == 3:
            if xs[0] >= xs[1]:
                if xs[2] >= 0:
                    raise SyntaxError
                else:
                    first = xs[0]
                    end = xs[1]
                    step = xs[2]                
            else:
                first = xs[0]
                end = xs[1]
                step = xs[2]
                
        self.first = first
        self.end = end
        self.step = step
    
    def __contains__(self,x):
        num = self.first
        while num < self.end:
            if x == num:
                return True
            num += self.step
        return False
        
    def __str__(self):
        return "class MyRange"
    
    def __iter__(self):
        self.num = self.first
        return self
    
    def __next__(self):
        if self.num < self.end:
            result = self.num
            self.num += self.step
            return result
        else:
            raise StopIteration            
        
    def __getitem__(self,i):
        if i >= self.__len__():
            raise IndexError       
        count = 0
        num = self.first
        while count <= i:
            result = num
            num += self.step
            count += 1
        return result
    
    def __len__(self):
        tmp_end = self.end // self.step
        tmp_first = self.first // self.step
        return tmp_end-tmp_first

mr = MyRange(5,10,2)
print("str:",str(mr))
print(4 in mr)
for i in mr:
    print(i)
print("len:",len(mr))
print("item:",mr[1])

