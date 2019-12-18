import pylab
import random,math
# ヒストグラム作成
pylab.hist([1,1,2,2,2,3,4,5,5,5,6,6,6,6,6])
pylab.show()

# 標準正規分布のヒストグラム
sum([random.gauss(0,1) for _ in range(10000)])/10000

for _ in range(10):
    print(sum([random.gauss(0,1) for _ in range(10000)])/10000)

pylab.hist([random.gauss(0,1) for _ in range(10000)],bins=50)
pylab.show()

# グラフ作成
pylab.plot([1,2,3,6],[1,4,9,36])
pylab.show()

# cosグラフ作成
xs=[x/100 for x in range(1000)]
ys=[math.cos(x) for x in xs]
pylab.plot(xs,ys)
pylab.show()

# 正規分布のグラフをplot
xp=[x/100 for x in range(-400,401)]
yp=[(1/2*math.pi*1)*math.exp(-(x-0)**2/2*1) for x in xp]
pylab.plot(xp,yp)
pylab.show()
