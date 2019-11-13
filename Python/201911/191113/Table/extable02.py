from basetable02 import Table

class ExTable(Table):
    def __init__(self,xss=[[]],*,type=object):
        Table.__init__(self,xss)
        if not all(all(isinstance(x,type) for x in xs if x != None) for xs in xss):
            raise ValueError(f"データ型が{type}ではないデータが含まれています")
        self.__type = type
    
    @property
    def get_type(self):
        return self.__type

    def get_list(self):
        """親Tableクラスのリストから2次元配列を得る関数"""
        def check(x,y):
            """辞書内の要素をチェックして値を返す関数
               @param x 座標x
               @param y 座標y
               @return  該当する要素があればその値、なければNone"""
            if (y,x) in self.get_dict:
                return self.get_dict[y,x]

        return [[check(x,y) for x in range(self.get_max_column)] 
                for y in range(self.get_max_row)]

    def erase_column(self,column):
        self._validate_axis_x_index(column,True)
        tmp_dic = {(y,x-1 if x>column else x):value
                    for ((y,x),value) in self.get_dict.items()
                    if x != column}
        self.replace_dict(tmp_dic)

    def erase_row(self,row):
        self._validate_axis_y_index(row,True)
        tmp_dic = {(y-1 if y>row else y,x):value
                    for ((y,x),value) in self.get_dict.items()
                    if y != row}
        self.replace_dict(tmp_dic)

    def insert_column(self, column):
        self._validate_axis_x_index(column,True)
        tmp_dic = {(y,x+1 if x>=column else x):value
                    for ((y,x),value) in self.get_dict.items()}
        self.replace_dict(tmp_dic)

    def insert_row(self, row):
        self._validate_axis_y_index(row,True)
        tmp_dic = {(y+1 if y>=row else y,x):value
                    for ((y,x),value) in self.get_dict.items()}
        self.replace_dict(tmp_dic)

    def transpose(self):
        tmp_dic = {(j,i):value for (i,j),value in self.get_dict.items()}        
        self.replace_dict(tmp_dic)
        
    def __setitem__(self, index, value):
        if not isinstance(value,self.__type):
            raise ValueError(f"データ型が{self.__type}ではありません")        
        super().__setitem__(index, value)
