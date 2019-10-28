# Scikit learnのサンプル学習データを取り込む
from sklearn import datasets

# 描画のためにmatplotlibモジュールを取り込む
from matplotlib import pyplot as plt, cm

# 手書き数字データを読み込む
digits = datasets.load_digits()
data = digits.images[0]

# 描画
plt.imshow(data.reshape(8,8),cmap=cm.gray_r,interpolation="nearest")
plt.show()