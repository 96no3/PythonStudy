class List(list):
    def append(self,x):
        if isinstance(x,int):
            self.insert(0,x)
        else:
            # 親クラスのメソッドを利用
            super().append(x)
            #list.append(self,x)

# 多重継承について
class Interface:
    def even(self):
        return len(self) % 2 == 0

class List2(list,Interface):
    pass

class Num(int):
    def __getitem__(self,index):
        return self + index

