class Table:
    def __init__(self,xss=[[]]):
        """リストを表として整形する
           @param xss  表示したいリスト（行の要素ごとをリストとする）"""        
        if not all([isinstance(xs,list) for xs in xss]):
            Table.err()

        def make_string(d):
            tmp_cell_list = list(d.keys())
            n = range(len(tmp_cell_list))
            tmp_y,tmp_x=0,0
            for i in n:
                if tmp_y < tmp_cell_list[i][0]:
                    tmp_y = tmp_cell_list[i][0]
                if tmp_x < tmp_cell_list[i][1]:
                    tmp_x = tmp_cell_list[i][1]

        
        if xss == [[]]:
            tmp_str,tmp_dict = "++\n++",{}
        else:
            tmp_y = len(xss)
            tmp_x = max([len(ys) for ys in yss])
            for y in tmp_y:
                for x in tmp_x:
                    tmp_dict[y,x] = xss[y][x]
            tmp_str = make_string(tmp_dict)

        self._table_dict = tmp_dict
        self._table_str = tmp_str
        self.f = make_string

    @staticmethod
    def err(message=""):
        raise SyntaxError(message)

    def __str__(self):
        return self._table_str

    def __contains__(self,value):
        return value in self._table_dict.values()

    def __getitem__(self,index):
        if index in self._table_dict:
            return self._table_dict[index]

    def __setitem__(self,index,value):
        if len(index) == 2:
            if all([isinstance(i,int) for i in index]):
                self._table_dict[index] = value
                self._table_str = self.f(self._table_dict)
            else:
                Table.err()
        else:
            Table.err()
