# ダック・タイピング(クラスの型が違えど同じメソッドがあれば同様に処理する)
from abc import ABCMeta,abstractmethod

# 抽象基底クラス
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def walk(self):
        pass

# あるインスタンスのsoundとwalkメソッドを実行
def test_duck(it):
    it.sound()
    it.walk()

class Duck(Animal):
    def sound(self):
        print("ガァガァ")
    def walk(self):
        print("アヒルが歩く")

class Dog(Animal):
    def sound(self):
        print("ワンワン")
    def walk(self):
        print("犬が歩く")

class Cat(Animal):
    def sound(self):
        print("ニャーニャー")
    def walk(self):
        print("猫が歩く")

ahiru = Duck()
test_duck(ahiru)

inu = Dog()
test_duck(inu)

neko = Cat()
test_duck(neko)