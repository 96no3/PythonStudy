class Table:    
    def __init__(self,xss=[[]]):
        self.__empty_type = ( None,[],(),{},"" )
        """リストを表として整形する
           @param xss  表示したい２次元リスト（行の要素ごとをリストとする）"""        
        if not all(isinstance(xs,list) for xs in xss):
            Table.err("要素がリスト型ではありません")
        
        self.__axis_y = len(xss)
        self.__axis_x = max(len(xs) for xs in xss) if xss else 0

        tmp_dic = {}            
        if xss != [[]]:
            for _y,xs in enumerate(xss):
                for _x,x in enumerate(xs):
                    if not x in self.__empty_type:
                        tmp_dic[_y,_x] = x

        self.__table_dict = tmp_dic

    def _validate_indexes(self, index, strict=False):
        try:
            _y,_x = index
        except:
            raise IndexError(f"{index}は不正なインデックスです")
            
        self._validate_axis_x_index(_x, strict)
        self._validate_axis_y_index(_y, strict)
        
    def _validate_axis_x_index(self, i, strict):
        Table.__validate_idx(i, self.__axis_x, strict)
 
    def _validate_axis_y_index(self, i, strict):
        Table.__validate_idx(i, self.__axis_y, strict)
 
    @staticmethod
    def __validate_idx(idx, maxnum, strict):
        """要素へアクセスするインデックスが利用可能かどうか調べる
           @param idx    辞書の要素へアクセスするインデックス
           @param max    登録されている要素の最大値
           @param strict 最大値の確認をするかどうかの真偽値"""
        if not isinstance(idx, int):
            raise IndexError(f"{idx}: インデックスは整数でなければなりません")
        if idx < 0 or (strict and idx >= maxnum):
            raise IndexError("out of range")

    def __make_string(self):
        """辞書に登録されている要素から表の文字列を作成する関数
           @param d ２次元配列の座標をタプルのキーとする辞書
           @return  辞書の座標に要素を入れて作成した表の文字列"""

        def check(x,y):
            """辞書内の要素をチェックして値を返す関数
               @param x 座標x
               @param y 座標y
               @return  該当する要素があればその値の文字列、
                        なければ' '(空白１つ)の文字列"""
            if (y,x) in self.__table_dict:
                if self.__table_dict[y,x] in self.__empty_type:
                    return " "
                else:
                    return str(self.__table_dict[y,x])                    
            else:
                return " "
            
        tmp_cell_list = list(self.__table_dict.keys())     
        if len(tmp_cell_list)==0:
            return "++\n++"
        
        tmp_list=[[check(x,y) for x in range(self.__axis_x)] for y in range(self.__axis_y)]            
        tmp_ps_list = [[len(tmp_list[y][x]) for y in range(self.__axis_y)]
                       for x in range(self.__axis_x)]            
        ps=[max(i) for i in tmp_ps_list]            
        str_line = Table.separator(("-" * i for i in ps),"+")
        str_table_list = [Table.separator(("%*s"%v for v in zip(ps,tmp_list[n])),"|")
                                                    for n in range(self.__axis_y)]
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

    def map(self,func):
        tmp_dict = dict()
        tmp_y, tmp_x = 0,0
        for ((i,j),x) in self.__table_dict.items():
            result = func(i,j,x)
            if result is not None:
                i,j,x = result
                idx = i,j
                self._validate_indexes(idx)
                tmp_y = max(i+1, tmp_y)
                tmp_x = max(j+1, tmp_x)
                tmp_dict[idx] = x
        self.__axis_y, self.__axis_x = tmp_y, tmp_x
        self.__table_dict = tmp_dict

    def replace_dict(self,dic):
        tmp_y,tmp_x = 0,0
        for y,x in dic.keys():
            tmp_y = max(y, tmp_y)
            tmp_x = max(x, tmp_x)
        self.__axis_y, self.__axis_x = tmp_y+1, tmp_x+1
        self.__table_dict = dic

    def get_list(self):
        """親Tableクラスのリストから2次元配列を得る関数"""
        def check(x,y):
            """辞書内の要素をチェックして値を返す関数
               @param x 座標x
               @param y 座標y
               @return  該当する要素があればその値、なければNone"""
            if (y,x) in self.__table_dict:
                return self.__table_dict[y,x]

        return [[check(x,y) for x in range(self.__axis_x)] 
                for y in range(self.__axis_y)]

    def __str__(self):
        return self.__make_string()

    def __contains__(self,value):
        return value in self.__table_dict.values()

    def __getitem__(self,index):
        self._validate_indexes(index, True)
        if index in self.__table_dict:
            return self.__table_dict[index]

    def __setitem__(self,index,value):
        self._validate_indexes(index)
        _y,_x = index
        self.__axis_y = max(_y+1,self.__axis_y)
        self.__axis_x = max(_x+1,self.__axis_x) 
        self.__table_dict[index] = value

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
    print(t2.get_max_column)
    print(t2.get_max_row)
    print(t2.get_dict)
