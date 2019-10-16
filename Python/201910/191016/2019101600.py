class MyClass:
    def func(self,a):
        return ("func",a)
    def _func(self,a):
        return ("_func",a)
    def __func(self,a):
        return ("__func",a)
    def test(self,a):
        return self.__func(a)

MyClass().func(0)
MyClass()._func(0)

#MyClass().__func(0) # private指定なのでエラー
MyClass().test(0) # クラス内部からの参照は可能

dir(MyClass())
# このように記述すれば非公開メンバにアクセス可能
MyClass()._MyClass__func(0)

# リスト内包とジェネレータ式
any([isinstance(x,int) for x in ["a",1,(1,2)]])
any(isinstance(x,int) for x in ["a",1,(1,2)])
all([isinstance(x,int) for x in [1,1,2]])
all(isinstance(x,int) for x in [1,1,2])
