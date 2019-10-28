## Scikit learnではじめる機械学習
* 定義済み学習データを利用
```
# Scikit learnのサンプル学習データを取り込む
from sklearn import datasets

# 手書き数字データを読み込む
digits = datasets.load_digits()
digits.images.shape # (1797,8,8) 手書きの数字データが1797件

# 0番目のデータ-どの数字か
digits.target[0]

# 0番目のピクセルデータ
digits.images[0]
```
<dl>
 <dt>targetプロパティ</dt>
 <dd>どの数字かを表すラベル情報のリスト</dd>
 <dt>imagesプロパティ</dt>
 <dd>ピクセルデータ(グレースケールの8x8ピクセル　16階調 0:薄い⇔15:濃い)