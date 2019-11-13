class SimpleCounter:
    @staticmethod
    def check_value(value):
        if not isinstance(value,int):
            raise ValueError(f"{value}は整数ではありません.")
    
    def __init__(self,value=0):
        SimpleCounter.check_value(value)
        self.__count = value

    def inc(self,value=1):
        SimpleCounter.check_value(value)
        self.__count += value
        
    def dec(self,value=1):
        SimpleCounter.check_value(value)
        self.__count -= value
        
    def count(self):
        return self.__count

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
            
        
