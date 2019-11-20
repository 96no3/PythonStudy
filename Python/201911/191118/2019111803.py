import functools as ft

class LinkedList:
    def __init__(self, x, tail):
        self.__head = x
        if isinstance(tail,LinkedList) or tail is None:
            self.__tail = tail
        else:
            raise ValueError(f'{tail}は連結できません')
        
    @property
    def head(self): ## 頭部を返す
        return self.__head
    
    @property
    def tail(self): ##　尾部を返す
        return self.__tail

    @head.setter
    def head(self,value):
        self.__head = value

    @tail.setter
    def tail(self,value):
        if isinstance(value,LinkedList) or value is None:
            self.__tail = value
        else:
            raise ValueError(f'{value}は連結できません')

    def set_tail(self,value):
        if isinstance(value,LinkedList) or value is None:
            self.__tail = value
        else:
            raise ValueError(f'{value}は連結できません')
        
    def __iter__(self): ## 再帰構造を辿るイテレータ(ジェネレータ)を生成
        def generator():
            obj = self
            while obj:
                yield obj.__head
                obj = obj.__tail
        return generator()

    def __next__(self):
        if self.__tail is None:
            raise StopIteration
        result = self.__head
        tmp = self.__tail        
        self.__head = tmp.head
        self.__tail = tmp.tail
        return result
 
    def __repr__(self): ## データ表現の文字列を生成
        result=None
        for x in reversed([*self]):
            result=f"LinkedList({repr(x)},{result})"
        return result
 
    def __str__(self): ## 表示用の文字列を生成
        return '(' + ' -> '.join(map(str,self)) + ')'
    
def make(iterable):
    return ft.reduce(lambda a,b:(b.set_tail(a),b)[1],
                     reversed([*(LinkedList(x,None) for x in iterable)]))
