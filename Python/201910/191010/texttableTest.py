from texttable import Texttable

xs = [[i*j for i in range(1,10)] for j in range(1,10)]
column=[x for x in range(1,9)]
#xs.insert(0,column)
table = Texttable()
#table.set_cols_align(["l", "r", "c"])
#table.set_cols_valign(["t", "m", "b"])
table.add_rows(xs)
print (table.draw() + "\n")
