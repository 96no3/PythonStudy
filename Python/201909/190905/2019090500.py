def make_num_list(num,count):
    """基となるnum文字列から連続した数をリスト化する関数
       @param num 基にするchar文字列
       @param count 作成したいリストの要素数
       @return _num_list num文字列リスト"""    
    _num_list = []
    _base = ord(str(num).lower())
    for i in range(count):
        _num_list.append(chr(_base))
        _base += 1
    return _num_list

xs=make_num_list("0",10)
print(xs)
