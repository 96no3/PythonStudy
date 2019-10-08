class MyRange:
    def __init__(self,*xs):
        first,end,step = MyRange.check(xs)
        self.first = first
        self.end = end
        self.step = step

    @staticmethod
    def err(message=""):
        raise SyntaxError(message)

    @staticmethod
    def check(xs):
        first,step = 0,1
        n = len(xs)
        if n == 0 or n > 3:
            MyRange.err()
        elif n == 1:
            if xs[0] <= 0 or not isinstance(xs[0],int):
                MyRange.err()
            else:
                end = xs[0]            
        elif n == 2:
            if not isinstance(xs[0],int) or not isinstance(xs[1],int):
                MyRange.err()
            elif xs[0] >= xs[1]:
                MyRange.err()            
            else:
                first = xs[0]
                end = xs[1]
        elif n == 3:
            if not isinstance(xs[0],int) or not isinstance(xs[1],int)\
               or not isinstance(xs[2],int):                
                MyRange.err()
            if xs[0] >= xs[1] or xs[2] <= 0:
                MyRange.err()                
            else:
                first = xs[0]
                end = xs[1]
                step = xs[2]                
        return first,end,step
    
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

mr = MyRange(2,10,3)
print("str:",str(mr))
print(4 in mr)
for i in mr:
    print(i)
print([*MyRange(2,10,3)])
print("len:",len(mr))
print("item:",mr[1])

