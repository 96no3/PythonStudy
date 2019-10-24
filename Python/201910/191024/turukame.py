# ダック・タイピング(クラスの型が違えど同じメソッドがあれば同様に処理する)
from abc import ABCMeta,abstractmethod

# 抽象基底クラス
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def legs(self):
        pass

class Turu(Animal):
    def name(self):
        return "鶴"
    def legs(self):
        return 2

class Kame(Animal):
    def name(self):
        return "亀"
    def legs(self):
        return 4

class Tako(Animal):
    def name(self):
        return "タコ"
    def legs(self):
        return 8

class Ika(Animal):
    def name(self):
        return "イカ"
    def legs(self):
        return 10

# 鶴亀算を解く関数
def calc_turukame(animal1,animal2,heads,legs):
    _a1leg = animal1.legs()
    _a2leg = animal2.legs()
    _a1name = animal1.name()
    _a2name = animal2.name()

    """ 実際の足の数と仮にすべてanimal1だと仮定した場合の足の数との差を計算し、
    それをanimal1とanimal2の足の数の差で割ると、animal2の数になる"""
    _a2num = (legs - (_a1leg * heads)) // (_a2leg - _a1leg)
    _a1num = heads - _a2num
    print("---")
    print("頭＝",heads,"足＝",legs)
    print(_a1name,"=",_a1num)
    print(_a2name,"=",_a2num)
    return (_a1num, _a2num)

# モジュールでない時は以下を実行
if __name__ == "__main__":
    # 鶴亀算で問題を解く
    calc_turukame(Turu(),Kame(),heads=10,legs=28)
    calc_turukame(Tako(),Ika(),heads=11,legs=100)
