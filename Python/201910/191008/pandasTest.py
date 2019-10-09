import numpy as np
import pandas as pd

def show(first=1,end=9):
    column=[]
    for i in range(first,end+1):
        column.append(i)
    v = np.matrix(range(first,end+1))
    v = np.transpose(v)*v
    df = pd.DataFrame(v, index=column, columns=column)
    print(df)

show()
show(4)
show(10,15)
