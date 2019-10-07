# ファイルの読み書き＜手順に注意＞

# 1. ファイルを開く
#a_file = open("test.txt",encoding = "utf-8")
#a_file = open("test.txt",mode="w",encoding = "utf-8")
a_file = open("test.txt",mode="a",encoding = "utf-8")

# 2. ファイルを読み書きする
try:
    #s= a_file.read()
    a_file.write("hoge\n")
    a_file.write("1234\nあああああああああああ\n")
    a_file.write("/*-\n")
    
# 3. ファイルを閉じる
finally:
    a_file.close()

#print(s)
