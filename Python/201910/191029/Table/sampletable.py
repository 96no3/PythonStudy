class Table:
    def __init__(self, xss=[]):
        if not isinstance(xss, list) or \
           not all(isinstance(xs, list) for xs in xss):
            raise ValueError
 
        self.n_row = len(xss)
        self.n_column = max(len(xs) for xs in xss) if xss else 0
        hash_table = dict()
 
        for i,xs in enumerate(xss):
            for j,x in enumerate(xs):
                 hash_table[i,j] = x
 
        self.hash_table = hash_table
 
    def _validate_indexes(self, indexes, strict=False):
        try:
            i,j = indexes
        except:
            raise IndexError(f"{indexes}は不正なインデックスです")
            
        self._validate_row_index(i, strict)
        self._validate_column_index(j, strict)
        
    def _validate_row_index(self, i, strict):
        self.__validate_idx(i, self.n_row, strict)
 
    def _validate_column_index(self, i, strict):
        self.__validate_idx(i, self.n_column, strict)
 
    @staticmethod
    def __validate_idx(idx, n, strict):
        if not isinstance(idx, int):
            raise IndexError(f"{idx}: インデックスは整数でなければなりません")
        if idx < 0 or strict and idx >= n:
            raise IndexError("out of range")
 
    def __setitem__(self, indexes, value):
        self._validate_indexes(indexes)
        i,j = indexes
        self.n_row, self.n_column = max(i+1,self.n_row), max(j+1,self.n_column)
        self.hash_table[i,j] = value
 
    def __getitem__(self, indexes):
        self._validate_indexes(indexes, True)
        if indexes in self.hash_table:
            return self.hash_table[indexes]
 
    def __str__(self):
 
        # ここを実装する
        def item(i,j):
            if (i,j) in self.hash_table:
                if self.hash_table[i,j] in ( None,[],(),{},"" ):
                    return " "
                else:
                    return str(self.hash_table[i,j])                    
            else:
                return " "
 
        def join(delim, strs):
                return delim + delim.join(strs) + delim
        def join_with_newline(delim, strs):
            d = delim+'\n'
            return d + d.join(s+'\n' for s in strs) + delim
 
        r_row, r_column = range(self.n_row), range(self.n_column)
        xss = [[item(i,j) for j in r_column] for i in r_row]
        widths = [max(len(xss[i][j]) for i in r_row) for j in r_column]
        bar = join('+', ('-'*w for w in widths))
        rows = [join('|', ('%*s' % z for z in zip(widths,xs))) for xs in xss]
 
        return join_with_newline(bar, rows)
