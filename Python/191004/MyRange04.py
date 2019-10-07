class MyRange:
    def __init__(self,*xs):
        first,end,step,f = self.check(xs)
        self.first = first
        self.end = end
        self.step = step
        self.f = f

    @staticmethod
    def err(message=""):
        raise SyntaxError(message)
    
    def iteration(self,step):
        def proc():            
            if step > 0:
                if self.num < self.end:
                    result = self.num
                    self.num += step
                    return result
                else:
                    raise StopIteration
            else:
                if self.num > self.end:
                    result = self.num
                    self.num += step
                    return result
                else:
                    raise StopIteration
        return proc
        
    def check(self,xs):
        first,step = 0,1
        is_num = lambda x:isinstance(x,int)
        n = len(xs)
        if n == 0 or n > 3 or not is_num(xs[0]):
            MyRange.err()
        elif n == 1:
            if xs[0] <= 0:
                end = 0
            else:
                end = xs[0]            
        elif n == 2:
            if not is_num(xs[1]):
                MyRange.err()
            elif xs[1] <= xs[0]:
                end = 0
            else:
                first = xs[0]
                end = xs[1]
        elif n == 3:
            if not is_num(xs[1]) or not is_num(xs[2]) or xs[2] == 0:                
                MyRange.err()            
            else:
                first = xs[0]
                end = xs[1]
                step = xs[2]
        f = self.iteration(step)
        return first,end,step,f
    
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
        return self.f()      
        
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
        tmp_max = max([tmp_first,tmp_end])
        tmp_min = min([tmp_first,tmp_end])
        return tmp_max - tmp_min

mr = MyRange(20,-8,-5)
print("str:",str(mr))
print(4 in mr)
for i in mr:
    print(i)
print([*MyRange(20,-8,-5)])
print("len:",len(mr))
print("item:",mr[1])

