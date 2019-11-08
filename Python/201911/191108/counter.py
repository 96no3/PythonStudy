class SimpleCounter:
    @staticmethod
    def err(x):
        if not isinstance(x,int):
            raise ValueError(f"{x}は整数ではありません.")
    
    def __init__(self,x=0):
        SimpleCounter.err(x)
        self.__x = x

    def inc(self,x=1):
        SimpleCounter.err(x)
        self.__x += x
        
    def dec(self,x=1):
        SimpleCounter.err(x)
        self.__x -= x
        
    def count(self):
        return self.__x

class Counter(SimpleCounter):
    def __repr__(self):
        return f"<Counter:{self.count()}>"
    
    def __str__(self):
        return f"<Counter:{self.count()}>"

    def __eq__(self,other):
        if isinstance(other,SimpleCounter):
            return self.count() == other.count()
        elif isinstance(other,int):
            return self.count() == other
        return False
            
        
