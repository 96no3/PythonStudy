from random import randint as rand
from time import time

class Question:
    def __init__(self):
        self._list=[]
        self._maxNum=9

g_q=[]
for i in range(4):
    g_q.append(Question())
    if i==0:
        g_q[i]._list=["a", "b", "a*b"]
    elif i==1:
        g_q[i]._list=["a", "b", "c", "a*b+c"]
        g_q[i]._maxNum = 19
    elif i==2:
        g_q[i]._list=["a", "b", "c", "d", "a+b*c+d"]
        g_q[i]._maxNum = 99
    else:
        g_q[i]._list=["a", "b", "c", "d", "a*b+c*d"]
        g_q[i]._maxNum = 999    

def input_difficulty():
    """入力を求める関数"""
    print("0:簡単 1:普通 2:難しい 3:激難")
    return input("0~3の範囲で難易度を入力してください:")

def get_difficulty_int(function):
    """＜高階関数＞入力を求める関数の値を判断する関数
       @param function 入力処理を行う関数
       @return s 認識可能なstring"""
    while True:
        s = function()        
        if s.lower() == "exit":
            break
        if s.isdigit():
            n=int(s)
            if n<0 or n > 3:
                print(f"「{n}」は0~3の数ではありません\n正しい入力値をお願いします")            
            else:
                return int(s)
        else:
            print(f"「{s}」は正の数値ではありません\n正しい入力値をお願いします")
    return "exit"

def input_num():
    """入力を求める関数"""
    return input("問題の出題数を入力してください：")

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
    
def Make99Question(difficultyNum):
    """九九問題を生成する関数
       @retval タプル(作成した問題のリスト,隠す場所の整数)"""
    question = g_q[difficultyNum]
    a = RandNum(question._maxNum)
    b = RandNum(question._maxNum)
    c = RandNum(question._maxNum)
    d = RandNum(question._maxNum)    
    results = list(map(eval,question._list))
    pos = RandPos(len(results)) # マジックナンバーを使わすシーケンスの長さで汎用性向上
    return (results,pos,question)

def Input99Question(results,pos,question):
    """九九の問題を表示し入力値を判断する関数
       @param results 九九問題のリスト
       @param pos     リストで隠す場所の要素番号
       @retval s     入力値の整数"""
    tmps = results.copy()
    tmps[pos] = '?'
    n = len(question._list)
    tmp_q = question._list[n-1]
    q_list = list(tmp_q)
    q_list[0] = tmps[0]
    q_list[2] = tmps[1]
    if len(q_list) > 3:
        q_list[4]=tmps[2]
    if len(q_list) > 5:
        q_list[6] = tmps[3]

    def GetAnswer():
        """入力値を返す関数
　　　　　　@retval 入力値の文字列"""
        for i in range(len(q_list)):
            print(q_list[i],end=" ")        
        s = input(f"= {tmps[len(tmps)-1]}:")
        return s

    return get_int(GetAnswer)
    
def Execution99Question(difficultyNum):
    """九九の問題を処理する関数
       @retval result 回答に対する真偽値(0:false 1:true)"""
    results,pos,question = Make99Question(difficultyNum)
    ans = Input99Question(results,pos,question)
    solution = results[pos]
    result = (ans==solution)
    print({False:"不正解…",True:"正解！"}[result])    # Dictionaryで結果を表示
    return result

def Do99Game(difficultyNum,num):
    """九九の問題を実行する関数
       @param num 繰り返し回数"""
    startTime = time()
    successNum = 0
    for i in range(num):
        print(f"\n{i+1}問目")
        successNum += Execution99Question(difficultyNum)
    endTime = time()
    deltaTime = round(endTime - startTime, 2)
    print(f"\n正解した数：{successNum} / {num}")
    print(f"あなたの正答率は{int(100*successNum/num)}%でした")
    print(f"回答時間は{deltaTime}秒でした")
    print(f"1問あたりの回答時間は{round(deltaTime/num, 2)}秒でした")


"""実行処理"""
Do99Game(get_difficulty_int(input_difficulty),get_int(input_num))
