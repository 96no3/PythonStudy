class TableShow:
    def __init__(self,*xs,index=None,column=None,mode=0):
        """リストを表として整形する
           @param *xs    表示したいリスト（行の要素ごとをリストとする）
           @param index  1列目に表示するリスト(mode=1 指定なしで要素数)
           @param column 1行目に表示するリスト(mode=1 指定なしで要素数)
           @param mode   indexとcolumnを含めるか(default=0 含めない)"""
        if not isinstance(xs,list):
            return SyntaxError
        if not all([isinstance(x,list) for x in xs]):
            result = " ".join([str(x) for x in xs])
        else:
            n = range(len(xs))
            ps=[len(str(x)) for x in xs[-1]]
            str_table_list=["|".join(line)
                    for line in [["%*d"%v for v in zip(ps,xs[n])]
                                 for n in range(len(column))]]

        self.string = result        

    def show(self,*,mode=0):
        """リストの表を得る関数
           @param  mode       返す値をstring型にするかどうか(default=0)
           @return mode=0     表をprint表示する(return None)
                   mode=0以外 表をstring型として返す"""
        if mode == 0:
            print(self.string)
        else:
            return self.string
        
        
