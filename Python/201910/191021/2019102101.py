# 演算子のオーバーロード
class Pos:
    """座標を表すクラス"""
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        """「+」演算子の振る舞いを定義
           selfとotherの要素を足した
           新しいインスタンスを返す"""
        x2 = self.x + other.x
        y2 = self.y + other.y
        return Pos(x2,y2)

    def __sub__(self,other):
        """「-」演算子の振る舞いを定義"""
        x2 = self.x - other.x
        y2 = self.y - other.y
        return Pos(x2,y2)

    def __mul__(self,other):
        """「*」演算子の振る舞いを定義"""
        if isinstance(other,(int,float)):
            x2 = self.x * other
            y2 = self.y * other
            return Pos(x2,y2)
        else:
            raise TypeError

    def __truediv__(self,other):
        """「/」演算子の振る舞いを定義"""
        if isinstance(other,(int,float)):
            x2 = self.x / other
            y2 = self.y / other
            return Pos(x2,y2)
        else:
            raise TypeError

    def __floordiv__(self,other):
        """「//」演算子の振る舞いを定義"""
        if isinstance(other,(int,float)):
            x2 = self.x // other
            y2 = self.y // other
            return Pos(x2,y2)
        else:
            raise TypeError

    def __mod__(self,other):
        """「%」演算子の振る舞いを定義"""
        if isinstance(other,(int,float)):
            x2 = self.x % other
            y2 = self.y % other
            return Pos(x2,y2)
        else:
            raise TypeError

    def __lt__(self,other):
        """「<」演算子の振る舞いを定義"""
        dis = self.x * self.x + self.y * self.y
        if isinstance(other,(int,float)):            
            if dis < other * other:
                return True
            else:
                return False
        elif isinstance(other,Pos):
            dis2 = other.x * other.x + other.y * other.y
            if dis < dis2:
                return True
            else:
                return False            
        else:
            raise TypeError

    def __le__(self,other):
        """「<=」演算子の振る舞いを定義"""
        dis = self.x * self.x + self.y * self.y
        if isinstance(other,(int,float)):            
            if dis <= other * other:
                return True
            else:
                return False
        elif isinstance(other,Pos):
            dis2 = other.x * other.x + other.y * other.y
            if dis <= dis2:
                return True
            else:
                return False            
        else:
            raise TypeError

    def __eq__(self,other):
        """「==」演算子の振る舞いを定義"""
        dis = self.x * self.x + self.y * self.y
        if isinstance(other,(int,float)):            
            if dis == other * other:
                return True
            else:
                return False
        elif isinstance(other,Pos):
            dis2 = other.x * other.x + other.y * other.y
            if dis == dis2:
                return True
            else:
                return False            
        else:
            raise TypeError

    def __ne__(self,other):
        """「!=」演算子の振る舞いを定義"""
        dis = self.x * self.x + self.y * self.y
        if isinstance(other,(int,float)):            
            if dis != other * other:
                return True
            else:
                return False
        elif isinstance(other,Pos):
            dis2 = other.x * other.x + other.y * other.y
            if dis != dis2:
                return True
            else:
                return False            
        else:
            raise TypeError

    def __gt__(self,other):
        """「>」演算子の振る舞いを定義"""
        dis = self.x * self.x + self.y * self.y
        if isinstance(other,(int,float)):            
            if dis > other * other:
                return True
            else:
                return False
        elif isinstance(other,Pos):
            dis2 = other.x * other.x + other.y * other.y
            if dis > dis2:
                return True
            else:
                return False            
        else:
            raise TypeError
        
    def __ge__(self,other):
        """「>=」演算子の振る舞いを定義"""
        dis = self.x * self.x + self.y * self.y
        if isinstance(other,(int,float)):            
            if dis >= other * other:
                return True
            else:
                return False
        elif isinstance(other,Pos):
            dis2 = other.x * other.x + other.y * other.y
            if dis >= dis2:
                return True
            else:
                return False            
        else:
            raise TypeError

    def __str__(self):
        """文字列として取得する際の振る舞いを定義"""
        return f"({self.x},{self.y})"

p1 = Pos(3,4)
p2 = Pos(30,40)
print("p1 < 5:",p1 < 5)
print("p1 <= 5:",p1 <= 5)
print("p1 == p2:",p1 == p2)
print("p1 != p2:",p1 != p2)
print("p1 > 5:",p1 > 5)
print("p1 >= 5:",p1 >= 5)
p3 = p1 + p2
print("p1 + p2:",p3)
p4 = p3 * 1.7
print("p3 * 1.7:",p4)
p5 = p1 - p2
print("p1 - p2:",p5)
p6 = p3 / 2
print("p3 / 2:",p6)
p6 = p3 // 2
print("p3 // 2:",p6)
p6 = p3 % 2
print("p3 % 2:",p6)
