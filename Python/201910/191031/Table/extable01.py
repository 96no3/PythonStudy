from basetable01 import Table

class ExTable(Table):
    def __init__(self,xss=[[]],*,type=object):
        Table.__init__(self,xss)
        if not all(all(isinstance(x,type) for x in xs if x != None) for xs in xss):
            raise ValueError(f"データ型が{type}ではないデータが含まれています")
        self._type = type
        self.get_list()

    def reset_dict(self,xss):
        if all(all(x == None for x in xs) for xs in self._table_list):
            self._table_list.clear()
        Table.__init__(self,self._table_list)

    def get_list(self):
        """親Tableクラスのリストから2次元配列を得る関数"""
        def check(x,y):
            """辞書内の要素をチェックして値を返す関数
               @param x 座標x
               @param y 座標y
               @return  該当する要素があればその値、なければNone"""
            if (y,x) in self._table_dict:
                return self._table_dict[y,x]                    

        tmp_dict={}
        for index,value in self._table_dict.items():
            if value != None:
                tmp_dict[index] = value            
        self._table_dict = tmp_dict

        tmp_cell_list = list(self._table_dict.keys())
        n = range(len(tmp_cell_list))           
        tmp_y,tmp_x = 0,0
        for i in n:
            if tmp_y < tmp_cell_list[i][0]:
                tmp_y = tmp_cell_list[i][0]
            if tmp_x < tmp_cell_list[i][1]:
                tmp_x = tmp_cell_list[i][1]
                
        self._axis_x, self._axis_y = tmp_x+1, tmp_y+1
        self._table_list = [[check(x,y) for x in range(self._axis_x)]\
             for y in range(self._axis_y)]        
        return self._table_list

    def erase_column(self,column):
        self._validate_axis_x_index(column,True)
        for xs in self._table_list:
            xs.remove(xs[column])
        self.reset_dict(self._table_list)
        self.get_list()
        self.reset_dict(self._table_list)

    def erase_row(self,row):
        self._validate_axis_y_index(row,True)
        self._table_list.remove(self._table_list[row])        
        self.reset_dict(self._table_list)
        self.get_list()
        self.reset_dict(self._table_list)
        
    def transpose(self):
        tmp_dict={}
        for index,value in self._table_dict.items():
            _y,_x = index
            self._axis_y = max(_x+1,self._axis_y)
            self._axis_x = max(_y+1,self._axis_x)
            trans = _x,_y
            tmp_dict[trans] = value
        self._table_dict = tmp_dict
        self.get_list()
        
    def __setitem__(self, index, value):
        if not isinstance(value,self._type):
            raise ValueError(f"データ型が{self._type}ではありません")        
        super().__setitem__(index, value)
        self.get_list()
