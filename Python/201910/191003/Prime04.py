class Prime:
    def __init__(self,x=100):
        """@param x 最大値とする閾値(default=100)"""
        if not Prime.is_num(x):
            raise ValueError        
        self._x = x

    @staticmethod
    def is_num(x):
        return isinstance(x,int)
    
    @property
    def threshold(self):
        return self._x
    
    @threshold.setter
    def threshold(self,value):
        if not Prime.is_num(value):
            raise ValueError
        self._x = value
        
    def __str__(self):
        return "prime numbers"

    def make_list(self):
        tmp = []
        n = self._x // 2
        for i in range(n):
            if i == 0:
                tmp.append(2)
            else:
                tmp.append(i*2+1)                    
        return tmp
    
    def __iter__(self):
        self._num = 2
        self._list = self.make_list()
        return self
    
    def __next__(self):
        print("debug:",self._list)
        count = 0
        count += 1
        num = self._num
        max_num = self._list[-1]
        while num < max_num:

            
            if num >= self._x:
                raise StopIteration
        return self._list[0]

# 処理時間を計測するデコレータ関数の定義
def time_log(func):
    def wrapper(*args,**kwargs):
        import datetime
        start = datetime.datetime.today()
        print("---start:" + func.__name__)
        res = func(*args,**kwargs)
        end = datetime.datetime.today()
        delta = end - start
        print("\n---end:" + func.__name__,delta,"sec")
        return res
    return wrapper

p = Prime()
print("str:",str(p))
print("threshold:",p.threshold)

@time_log
def test_iter():
    for i in p:
        print(i)

test_iter()

p.threshold = 10000
print("\nthreshold:",p.threshold)
test_iter()



    


