def moment(xs,m,u=0):
    return sum((x-u)**m for x in xs) / len(xs)

xs=[*range(1,101)]
moment(xs,1) # 平均値
moment(xs,2,moment(xs,1)) # 分散
# 積率による分散の計算
moment(xs,2) - moment(xs,1)**2
