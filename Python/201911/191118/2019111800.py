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
        tmp="LinkedList("
        result=""
        count=0
        for i in map(str,self):
            result += tmp+i+","
            count+=1
        return result + "None"+")"*count
 
    def __str__(self): ## 表示用の文字列を生成
        return '(' + ' -> '.join(map(str,self)) + ')'
    
def make_LinkedList(*xs):
    n=len(xs)
    if n == 0:
        raise ValueError("引数に1つ以上の要素を入れてください")
    pre,result = None,None
    for s in xs:
        tmp = LinkedList(s,None)
        if pre:            
            pre.tail = tmp            
        else:
            result = tmp
        pre = tmp
    return result
