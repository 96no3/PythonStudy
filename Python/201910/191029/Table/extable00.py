from basetable import Table

class ExTable(Table):
    def __init__(self,xss=[[]],*,type=object):
        Table.__init__(self,xss)
        if not all(all(isinstance(x,type) for x in xs) for xs in xss):
            raise ValueError(f"データ型が{type}ではないデータが含まれています")
        self._type = type
        self.get_list()

    def reset_dict(self,xss):
        if(all(all(x == None for x in xs) for xs in self._table_list)):
            self._table_list.clear()
        Table.__init__(self,self._table_list)

    def get_list(self):
        """親Tableクラスのリストから2次元配列を得る関数"""
        def check(x,y,d):
            """辞書内の要素をチェックして値を返す関数
               @param x 座標x
               @param y 座標y
               @param d 辞書
               @return  該当する要素があればその値、なければNone"""
            if (y,x) in d:
                return d[y,x]

        tmp_cell_list = list(self._table_dict.keys())
        n = range(len(tmp_cell_list))           
        tmp_y,tmp_x = 0,0
        for i in n:
            if tmp_y < tmp_cell_list[i][0]:
                tmp_y = tmp_cell_list[i][0]
            if tmp_x < tmp_cell_list[i][1]:
                tmp_x = tmp_cell_list[i][1]
        self._table_list = [[check(x,y,self._table_dict) for x in range(tmp_x+1)] for y in range(tmp_y+1)]        
        return self._table_list

    def erase_column(self,column):
        if not isinstance(column,int) and 0 <= column < self._column:
            raise ValueError
        for xs in self._table_list:
            xs.remove(xs[column])
        self.reset_dict(self._table_list)

    def erase_row(self,row):
        if not isinstance(row,int) and 0 <= row < self._row:
            raise ValueError
        self._table_list.remove(self._table_list[row])
        self.reset_dict(self._table_list)
        
    def transpose(self):
        pass

    def swap(self,column,row):
        if not isinstance(column,int) and 0 <= column < self._column:
            raise ValueError
        if not isinstance(row,int) and 0 <= row < self._row:
            raise ValueError        
        _tmp = self._table_dict[column,row]
        self._table_dict[column,row] = self._table_dict[row,column]
        self._table_dict[row,column] = _tmp
        
    def __setitem__(self, index, value):
        if not isinstance(value,self._type):
            raise ValueError(f"データ型が{self._type}ではありません")        
        super().__setitem__(index, value)
        self.get_list()
