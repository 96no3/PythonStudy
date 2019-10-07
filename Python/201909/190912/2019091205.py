# with構文で自動的にclose()を呼ぶ
#with open("test.txt",mode="w",encoding="utf-8") as f:
#    f.write("I'm happy\n")
#    f.write("But I'm sad\n")

# テキストファイルを1行ずつ処理
#with open("test.txt",encoding="utf-8") as f:
#    for line in f:
#        print(line)

# テキストからキーワードを探す
key = "sad"
with open("test.txt",encoding="utf-8") as f:
    for i,line in enumerate(f):
        if line.find(key)>=0:
            print(i+1,":",line)
