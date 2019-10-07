import datetime
datetime.date.today()

t=datetime.datetime.now() # 現在時刻の取得
t.strftime("%Y/%m/%d %H:%M:%S") # 日時を出力

t + datetime.timedelta(weeks = 1) # 経過時間を加える(+)引く(-)

t1=datetime.date(2019,9,17)
t2=datetime.date(2019,4,17)
t3=t1-t2
