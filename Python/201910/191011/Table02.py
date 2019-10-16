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

            def check(x,y,d):
                """辞書内の要素をチェックして値を返す関数
                   @param x 座標x
                   @param y 座標y
                   @param d 辞書
                   @return  該当する要素があればその値の文字列、
                            なければ' '(空白１つ)の文字列"""
                if (y,x) in d:
                    if d[y,x] in ( None,[],(),{},"" ):
                        return " "
                    else:
                        return str(d[y,x])                    
                else:
                    return " "
            
            tmp_cell_list = list(d.keys())            
            if len(tmp_cell_list)==0:
                return "++\n++"
            n = range(len(tmp_cell_list))           
            tmp_y,tmp_x = 0,0
            for i in n:
                if tmp_y < tmp_cell_list[i][0]:
                    tmp_y = tmp_cell_list[i][0]
                if tmp_x < tmp_cell_list[i][1]:
                    tmp_x = tmp_cell_list[i][1]
            
            tmp_list=[[check(x,y,d) for x in range(tmp_x+1)] for y in range(tmp_y+1)]            
            tmp_ps_list = [[len(tmp_list[y][x]) for y in range(tmp_y+1)]
                           for x in range(tmp_x+1)]            
            ps=[max(i) for i in tmp_ps_list]            
            str_line = separator(["-" * i for i in ps],"+")
            str_table_list=["|".join(line) for line in [["%*s"%v for v in zip(ps,tmp_list[n])]
                                                        for n in range(tmp_y+1)]]
            tmp_str = ""
            for n in range(tmp_y+1):
                tmp_str += str_line + "\n"
                tmp_str += "|" + str_table_list[n]+ "|\n"
            tmp_str += str_line + "\n"
            return tmp_str
        
        tmp_dict = {}            
        if xss != [[]]:
            tmp_y = len(xss)
            ns = [len(xs) for xs in xss]
            tmp_x = max(ns)
            tmp_dict[tmp_y-1,tmp_x-1] = " "
            for y in range(tmp_y):
                _count = 0
                while _count < ns[y]:
                    tmp_dict[y,_count] = xss[y][_count]
                    _count += 1

        self._table_dict = tmp_dict
        self._f = make_string

    @staticmethod
    def err(message=""):
        raise SyntaxError(message)

    def __str__(self):
        return self._f(self._table_dict)

    def __contains__(self,value):
        return value in self._table_dict.values()

    def __getitem__(self,index):
        if index in self._table_dict:
            return self._table_dict[index]
        #else:
        #    Table.err()

    def __setitem__(self,index,value):
        if len(index) == 2:
            if all([isinstance(i,int) for i in index]):
                self._table_dict[index] = value                
            else:
                Table.err()
        else:
            Table.err()

t=Table()
print(t)
print(111 in t)
t[2,3]=111
print(t)
print(t[2,3])
print(111 in t)
print(t[2,1] is None)

t2=Table([[1,2,3,4,5],[0,111,"hello"],[6,7]])
print(t2)
t2[2,3]=111
print(t2)
t2[10,10]= 2
print(t2)
t2[10,10]+= 200
print(t2)
t2[11,11] = ()
print(t2)
#t2[1000,0]
#Table().err("test staticmethod")
