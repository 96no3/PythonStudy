from random import randint as rand
from time import time

def RandPos(posNum):
    """シークエンス内のある位置をランダムに取得する関数
       @param  posNum シークエンスの要素数
       @retval シークエンス内のある位置をあらわす数"""
    return rand(0,posNum-1)

def RandNum(maxNum):
    """2~maxNumまでの範囲の数をランダムに取得する関数
       @param maxNum 範囲の最大値
       @retval ランダムな整数"""
    return rand(2,maxNum)

def GetRandNum():
    """RandNum(maxNum)を用いて数をランダムに取得する関数
       @retval ランダムな整数"""
    return RandNum(9)
    
def Make99Question():
    """九九問題を生成する関数
       @retval タプル(作成した問題のリスト,隠す場所の整数)"""
    a,b,c = GetRandNum(),GetRandNum(),GetRandNum()
    results = [a, b, c, a * b + c]
    pos = RandPos(len(results)) # マジックナンバーを使わすシーケンスの長さで汎用性向上
    return (results,pos)

def get_int(function):
    """＜高階関数＞入力を求める関数の値を判断する関数
       @param function 入力処理を行う関数
       @return tmpNum 正しい入力値の数"""
    while True:
        s = function()
        if s.isdigit():
            return int(s)
        else:
            print(f"「{s}」は正の半角整数ではありません\n正しい入力値をお願いします")

def Input99Question(results,pos):
    """九九の問題を表示し入力値を判断する関数
       @param results 九九問題のリスト
       @param pos     リストで隠す場所の要素番号
       @retval s     入力値の整数"""
    tmps = results.copy()
    tmps[pos] = '?'

    def GetAnswer():
        """入力値を返す関数
　　　　　　@retval 入力値の文字列"""
        s = input(f"{tmps[0]} * {tmps[1]} + {tmps[2]} = {tmps[3]}:")
        return s

    return get_int(GetAnswer)
    
def Execution99Question():
    """九九の問題を処理する関数
       @retval result 回答に対する真偽値(0:false 1:true)"""
    results,pos = Make99Question()
    ans = Input99Question(results,pos)
    solution = results[pos]
    result = (ans==solution)
    print({False:"不正解…",True:"正解！"}[result])    # Dictionaryで結果を表示
    return result

def Do99Game(num):
    """九九の問題を実行する関数
       @param num 繰り返し回数"""
    startTime = time()
    successNum = 0
    for i in range(num):
        print(f"\n{i+1}問目")
        successNum += Execution99Question()
    endTime = time()
    deltaTime = round(endTime - startTime, 2)
    print(f"\n正解した数：{successNum} / {num}")
    print(f"あなたの正答率は{int(100*successNum/num)}%でした")
    print(f"回答時間は{deltaTime}秒でした")
    print(f"1問あたりの回答時間は{round(deltaTime/num, 2)}秒でした")

def input_num():
    """入力を求める関数"""
    return input("九九問題の出題数を入力してください：")

"""実行処理"""
Do99Game(get_int(input_num))

