r=range(1,10)
table=[[i*j for i in r] for j in r]
print(table)
ps = [len(str(x)) for x in table[-1]]
print(ps)
print("\n".join(["".join(line) for line in [["%*d|"%x for x in zip(ps,xs)] for xs in table]]))
