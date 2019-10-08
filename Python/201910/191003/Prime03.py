class Prime:
    def __init__(self,x=10,*,mode=0):
        """@param x     閾値(default=10)
           @param mode　0＝個数　1＝最大値（default=0）"""
        if not Prime.is_num(x) or not Prime.is_num(mode)\
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
        if not Prime.is_num(value) or (value < 0 or value > 1):
            raise ValueError
        self._mode = value

    @threshold.setter
    def threshold(self,value):
        if not Prime.is_num(value):
            raise ValueError
        self._x = value
        
    def __str__(self):
        return "prime numbers"
    
    def __iter__(self):
        self._count = 0
        self._num = 1
        return self
    
    def __next__(self):
        if self._mode == 0 and self._count >= self._x:
            raise StopIteration
        
        is_prime = False
        self._num += 1
        while not is_prime:            
            is_prime = True
            for i in range(2,self._num):
                if self._num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                break
            self._num += 1

            if self._mode == 1 and self._num >= self._x:
                raise StopIteration
        self._count += 1
        return self._num

# デコレータ関数の定義
def show_func_name(func):
    # 関数内で関数を定義する
    def wrapper(*args,**kwargs):
        # 前処理
        print("---start:" + func.__name__)
        # 関数の実行
        res = func(*args,**kwargs)
        # 後処理
        print("\n---end:" + func.__name__)
        return res
    # 関数オブジェクトを返す
    return wrapper

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
print("mode:",p.mode,"threshold:",p.threshold)

@time_log
def test_iter():
    for i in p:
        print(i,end=" ")

test_iter()

p.mode = 1
p.threshold = 200
print("\nmode:",p.mode,"threshold:",p.threshold)
test_iter()



    


