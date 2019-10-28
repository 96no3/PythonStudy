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
 <dd>ピクセルデータ(グレースケールの8x8ピクセル　16階調 0:薄い⇔15:濃い)</dd>
</dl>

```
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
```
<dl>
 <dt>matplotlibモジュール</dt>
 <dd>データの描画</dd>
</dl>

## 手書き数字認識
* **SVM**アルゴリズムを利用して機械学習
<dl>
 <dd>precision:精度、recall:再現率（実際に正解した割合）、fl-score:精度と再現率の調和平均、support:正解ラベルのデータ数</dd>
 <dt>precisionとrecallの違いは計算方法の違い</dt> 
 <dd>どちらも予測が正しいことの指標 </dd>
 <dd>モデルの判定結果が真かつ実際に正しい値を判定：True Positive(TP) 誤り：False Positive(FP)</dd>
 <dd>モデルの判定結果が偽かつ実際の値が真（予測と違う値）：False Negative(TN) 実際の値も偽：True Negative(TN)</dd>
 <dt>precision(適合率)の計算</dt>
 <dd>TP / (TP + FP)</dd>
 <dt>recall(再現率)の計算</dt>
 <dd>TP / (TP + FN)</dd>
</dl>

 |   |実際の値が真|実際の値が偽|
 |------------|-----------------|------------------|
 |判定結果が真|True Positive(TP)|False Positive(FP)|
 |判定結果が偽|False Negative(TN)|True Negative(TN)|

```
from sklearn import datasets,svm, metrics
from sklearn.model_selection import train_test_split

# 手書き数字データを読み込む
digits = datasets.load_digits()

# 訓練用データとテスト用データに分ける
data_train, data_test, label_train, label_test = \
    train_test_split(digits.data, digits.target)
    
# SVMアルゴリズムを利用してモデルを構築する
clf = svm.SVC(gamma=0.001)
clf.fit(data_train,label_train)

# テストデータでの分析結果予測してみる
predict = clf.predict(data_test)

# 結果を表示する
ac_score = metrics.accuracy_score(label_test,predict)
cl_report = metrics.classification_report(label_test,predict)
print("分類器の情報＝",clf)
print("正解率＝",ac_score)
print("レポート＝\n",cl_report)
```
<dl>
 <dt>train_test_split(digits.data, digits.target)</dt>
 <dd>指定されたデータをランダムに訓練用とテスト用のデータに分ける。</dd>
 <dd>手書き画像データ(digits.data)とラベルデータ(digits.target)を入力し、訓練用とテスト用のデータとラベルを出力</dd>
 <dt>svm.SVC(gamma=0.001)</dt>
 <dd>SVMアルゴリズムのSVCクラスを用いて分類。引数にパラメータを指定</dd>
 <dd>SVMには、SVC/LinearSVC/NuSVCなどの種類があり、SVCは標準的実装。LinearSVCは線形カーネルに特化し、高速に計算ができる。種類によって実行速度や判定精度が変わる</dd>
 <dd>引数のパラメータ：&nbsp;ガンマ値(gamma=)&emsp;ソフトマージンのコストパラメータを表す(C)など指定できる</dd>
 <dt>clf.fit(data_train,label_train)</dt>
 <dd>fit()メソッドの第一引数は訓練データの本体、第二引数は訓練データに対するラベルを指定して学習させる。</dd>
 <dt>clf.predict(data_test)</dt>
 <dd>predict()メソッドで学習済みモデルを元に、テストデータの分類を予測する。</dd>
