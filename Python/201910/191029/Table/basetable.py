class Table:
    def __init__(self,xss=[[]]):
        """リストを表として整形する
           @param xss  表示したい２次元リスト（行の要素ごとをリストとする）"""        
        if not all(isinstance(xs,list) for xs in xss):
            Table.err()
        
        self._row = len(xss)
        self._column = max(len(xs) for xs in xss) if xss else 0

        tmp_dict = {}            
        if xss != [[]]:
            for i,xs in enumerate(xss):
                for j,x in enumerate(xs):
                    tmp_dict[i,j] = x

        self._table_dict = tmp_dict

    @staticmethod
    def make_string(d):
        """辞書に登録されている要素から表の文字列を作成する関数
           @param d ２次元配列の座標をタプルのキーとする辞書
           @return  辞書の座標に要素を入れて作成した表の文字列"""

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
        str_line = Table.separator(("-" * i for i in ps),"+")
        str_table_list = [Table.separator(("%*s"%v for v in zip(ps,tmp_list[n])),"|")
                                                    for n in range(tmp_y+1)]
        return Table.join_with_newline(str_line, str_table_list)

    @staticmethod
    def err(message=""):
        raise SyntaxError(message)

    @staticmethod
    def separator(s,sep):
        """リスト内の文字列を指定した文字列で区切り、結合する関数
        @param s   文字列
        @param sep 区切りに使用する文字列
        @return    指定した文字列で区切り、要素を結合した文字列"""
        return sep + sep.join(s) + sep

    @staticmethod
    def join_with_newline(delim, strs):
        """リスト内の文字列を指定した文字列で区切り、結合する関数
        @param delim 上段に付足す文字列
        @param strs  文字列のリスト
        @return      文字列を上段に追加し、要素を結合した文字列"""
        d = delim + '\n'
        return d + d.join(s+'\n' for s in strs) + delim

    def __str__(self):
        return Table.make_string(self._table_dict)

    def __contains__(self,value):
        return value in self._table_dict.values()

    def __getitem__(self,index):
        if index in self._table_dict:
            return self._table_dict[index]

    def __setitem__(self,index,value):
        if len(index) == 2:
            if all(isinstance(i,int) for i in index):
                self._table_dict[index] = value                
            else:
                Table.err()
        else:
            Table.err()

if __name__ == "__main__":
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
