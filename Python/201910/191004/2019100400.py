import numpy as np
v = np.matrix(range(1,10))
print(v)

print(v[0])
print(v[0,[0]])
print(v[0,0])

print(np.transpose(v))
print(np.transpose(v)*v)

print(v * np.transpose(v))

xs=[i**2 for i in range(1,10)]
print(xs)

def test(xs):
    tmp = 0
    for i in xs:
        tmp += i
    print(tmp)

test(xs)
	
