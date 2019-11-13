from basetable03 import Table

class ExTable(Table):
    def __init__(self,xss=[[]],*,type=object):
        Table.__init__(self,xss)
        if not all(all(isinstance(x,type) for x in xs if x != None) for xs in xss):
            raise ValueError(f"データ型が{type}ではないデータが含まれています")
        self.__type = type
    
    @property
    def get_type(self):
        return self.__type    

    def erase_column(self,column):
        self._validate_axis_x_index(column,True)
        def f(y,x,value):
            if x != column:
                if x>column:
                    tmp = x-1
                    return y,tmp,value
                else:
                    return y,x,value
        self.map(f)

    def erase_row(self,row):
        self._validate_axis_y_index(row,True)
        def f(y,x,value):
            if y != row:
                if y>row:
                    tmp = y-1
                    return tmp,x,value
                else:
                    return y,x,value
        self.map(f)

    def insert_column(self, column):
        self._validate_axis_x_index(column,True)
        def f(y,x,value):
            if x>=column:
                tmp = x+1
                return y,tmp,value
            else:
                return y,x,value                
        self.map(f)

    def insert_row(self, row):
        self._validate_axis_y_index(row,True)
        def f(y,x,value):
            if y>=row:
                tmp = y+1
                return tmp,x,value
            else:
                return y,x,value                
        self.map(f)

    def transpose(self):
        def f(y,x,value):
            return x,y,value                
        self.map(f)
        
    def __setitem__(self, index, value):
        if not isinstance(value,self.__type):
            raise ValueError(f"データ型が{self.__type}ではありません")        
        super().__setitem__(index, value)
