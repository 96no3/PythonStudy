class Table:
    def __init__(self,xss=[[]]):
        """リストを表として整形する
           @param xss  表示したい２次元リスト（行の要素ごとをリストとする）"""        
        if not all([isinstance(xs,list) for xs in xss]):
            Table.err()

        def make_string(d):
            """辞書に登録されている要素から表の文字列を作成する関数
               @param d ２次元配列の座標をタプルのキーとする辞書
               @return  辞書の座標に要素を入れて作成した表の文字列"""
            
            def separator(xs,sep):
                """リスト内の文字列を指定した文字列で区切り、結合する関数
                   @param xs  文字列のリスト
                   @param sep 区切りに使用する文字列
                   @return    指定した文字列で区切り、要素を結合した文字列"""
                return sep + sep.join(xs) + sep
            
            tmp_cell_list = list(d.keys())
            n = range(len(tmp_cell_list))
            tmp_y,tmp_x = 0,0
            for i in n:
                if tmp_y < tmp_cell_list[i][0]:
                    tmp_y = tmp_cell_list[i][0]
                if tmp_x < tmp_cell_list[i][1]:
                    tmp_x = tmp_cell_list[i][1]
            
            tmp_list=[]            
            for y in range(tmp_y+1):
                tmp_list.append([])
                for x in range(tmp_x+1):
                    if (y,x) in d:
                        tmp_list[y].append(str(d[y,x]))
                    else:
                        tmp_list[y].append(" ")
                        
            tmp_ps_list=[]
            for x in range(tmp_x+1):
                tmp_ps_list.append([])
                for y in range(tmp_y+1):
                    tmp_ps_list[y].append(len(tmp_list[y][x]))

            tmp_ps=[max(i) for i in tmp_ps_list]

        
        if xss == [[]]:
            tmp_str,tmp_dict = "++\n++",{}
        else:
            tmp_y = len(xss)
            ns = [len(xs) for xs in xss]
            tmp_x = max(ns)
            tmp_dict[tmp_y-1,tmp_x-1] = " "
            for y in range(tmp_y):
                _count = 0
                while _count < ns[y]:
                    tmp_dict[y,_count] = xss[y][_count]
                    _count += 1
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
