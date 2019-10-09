r=range(1,10)
table=[[i*j for i in r] for j in r]
len(str(table[-1][-1]))
ps = [len(str(x)) for x in table[-1]]
[["%*d"%a for a in zip(ps,xs)] for xs in table]
[["%*d"%(p,x) for p,x in zip(ps,xs)] for xs in table]
