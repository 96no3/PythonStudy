from random import randint as rand

def OtherHand():
    """相手の手をランダムに出す関数
       @retval 0 グー
       @retval 1 チョキ
       @retval 2 パー"""
    otherHand = rand(0,2)
    hand = {0:"グー",1:"チョキ",2:"パー"}
    print(f"相手の手：{hand[otherHand]}")
#    if otherHand == 0:
#        print("相手の手：グー")
#    elif otherHand == 1:
#        print("相手の手：チョキ")
#    else:
#        print("相手の手：パー")
    return otherHand


def Janken(playerHand,otherHand):
    """ジャンケンの勝ち負け判断関数
       @retval 1 勝ち
       @retval 0 勝ち以外（負け、引き分け）"""
    x = (playerHand-otherHand+3) % 3
    
    if x==0:
        print("引き分け")
        return 0
    elif x==1:
        print("負け")
        return 0
    else:
        print("勝ち")
        return 1

def get_int(function):
    """＜高階関数＞入力を求める関数の値を判断する関数
       @param function 入力処理を行う関数
       @return tmpNum 正しい入力値の数"""
    while True:
        s = function()
        if s.isdigit():
            tmpNum = int(s)
            if tmpNum < 0 or tmpNum > 2:
                print(f"「{s}」は無効な数字です\n正しい入力値をお願いします")
            else:
                return tmpNum
        else:
            print(f"「{s}」は無効な数字です\n正しい入力値をお願いします")

def InputPlayerHand():
    """プレイヤー入力値を判断する関数
       @retval s     入力値の整数"""

    def GetAnswer():
        """入力値を返す関数
　　　　　　@retval 入力値の文字列"""
        print("0:グー、1:チョキ、2:パー")
        playerHand = input("出したい手を0～2で入力してね：")
        return playerHand

    return get_int(GetAnswer)
    
    # 入力値が正しい値かどうかを確認
#    while True:
#        playerHand = GetAnswer()
#        if playerHand.isnumeric():
#            tmpNum = int(playerHand)
#            if tmpNum < 0 or tmpNum > 2:
#                print(f"{playerHand}は無効な数字です")
#            else:
#                return tmpNum
#        else:
#            print("正しい入力値をお願いします")

def DoJanken(num):
    """ジャンケンを実行する関数
       @param num 繰り返し関数"""
    count = 0
    for i in range(num):
        print(f"\n{i+1}回目***じゃんけんスタート***")
        hand = InputPlayerHand()
        otherHand = OtherHand()
        count += Janken(hand,otherHand)
    print(f"\n勝った回数：{count} / {num}")

def input_num():
    """入力を求める関数"""
    return input("ジャンケンの回数を入力してください：")

#count = 0
#repeatNum = int(input("Please input repeat count:"))
#for i in range(repeatNum):
#    print("***じゃんけんスタート***")
    
    #print("0:グー、1:チョキ、2:パー")
    #playerHand = int(input("出したい手を0～2で入力してね："))
    #if playerHand < 0 or playerHand > 2:
    #    print(f"{playerHand}は無効な数字です")
    #else:
    #    otherHand = OtherHand()
    #    count += Janken(playerHand,otherHand)
    
#    hand = InputPlayerHand()
#    otherHand = OtherHand()
#    count += Janken(hand,otherHand)

#print(f"勝った回数：{count} / {repeatNum}")
    
"""実行処理"""
#repeatNum = int(input("Please input repeat count:"))
DoJanken(get_int(input_num))   
