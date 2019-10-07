from random import randint as rand
from time import time

def RandPos(posNum):
    """シークエンス内のある位置をランダムに取得する関数
       @param  posNum シークエンスの要素数
       @retval シークエンス内のある位置をあらわす数"""
    return rand(0,posNum-1)

def RandNum(maxNum):
    """1~maxNumまでの範囲の数をランダムに取得する関数
       @param maxNum 範囲の最大値
       @retval ランダムな整数"""
    return rand(1,maxNum)
    
def Make99Question():
    """九九問題を生成する関数
       @retval タプル(作成した問題のリスト,隠す場所の整数)"""
    a,b = RandNum(9),RandNum(9)
    results = [a, b, a * b]
    pos = RandPos(len(results)) # マジックナンバーを使わすシーケンスの長さで汎用性向上
    return (results,pos)

def Input99Question(results,pos):
    """九九の問題を表示し入力値を判断する関数
       @param results 九九問題のリスト
       @param pos     リストで隠す場所の要素番号
       @retval s     入力値の整数"""
    tmps = results.copy()
    tmps[pos] = '?'
    #print(f"{tmps[0]} * {tmps[1]} = {tmps[2]}")

    def GetAnswer():
        """入力値を返す関数
　　　　　　@retval 入力値の文字列"""
        s = input(f"{tmps[0]} * {tmps[1]} = {tmps[2]}:")
        return s
    
    # 入力値が正しい値かどうかを確認
    while True:
        s = GetAnswer()
        if s.isnumeric():
            return int(s)        
    
def Execution99Question():
    """九九の問題を処理する関数
       @retval result 回答に対する真偽値(0:false 1:true)"""
    results,pos = Make99Question()
    ans = Input99Question(results,pos)
    solution = results[pos]
    result = (ans==solution)
    print(("不正解…","正解！")[result])
    #if ans==solution:
        #print("正解！")
    #else:
        #print("不正解…")
    return result

def Do99Game(num):
    """九九の問題を実行する関数
       @param num 繰り返し回数"""
    startTime = time()
    successNum = 0
    for i in range(num):
        successNum += Execution99Question()
    endTime = time()
    deltaTime = endTime - startTime
    print(f"正解した数：{successNum} / {num}")
    print(f"あなたの正答率は{int(100*successNum/num)}%でした")
    print(f"回答時間は{deltaTime}秒でした")
    print(f"1問あたりの回答時間は{deltaTime/num}秒でした")


repeatNum = int(input("Please input repeat count:"))
#for i in range(repeatNum):
#    print(RandPos(num))

#results,pos = Make99Question()
#print(f"results = {results}")
#print(f"pos = {pos}")
#ans = Input99Question(results,pos)
#solution = results[pos]
#print(f"your answer is {ans}")
#print(f"the solution is {solution}")
#print(ans==solution)

#successNum = 0
#for i in range(n):
#    successNum += Execution99Question()
#print(f"正解した数：{successNum} / {n}")
#print(f"あなたの正答率は{int(100*successNum/n)}%でした")
Do99Game(repeatNum)
