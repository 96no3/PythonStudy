count = 0
def count_inc():
    global count
    count += 1

def count_dec():
    global count
    count -= 1

def count_get():
    global count
    return count

data_dic = {"cnt":0}
def cntdic_inc(dic):
    dic["cnt"] += 1

def cntdic_dec(dic):
    dic["cnt"] -= 1

def cntdic_get(dic):
    return dic["cnt"]
