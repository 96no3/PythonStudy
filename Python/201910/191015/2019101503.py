# 正規表現
import re # 正規表現reモジュールを取り込む
pat = r"\d+" # raw stringの記述
string = "This pen is 100yen."
repl = 200
# 正規表現検索 どこかにマッチするかを調べてmatchオブジェクトを返す。見つからない場合はNone
re.search(pat,string) 
# 文字列の先頭からマッチするかを調べてmatchオブジェクトを返す。見つからない場合はNone
re.match(pat,string) 
re.split(pat,string)
re.findall(pat,string)
re.finditer(pat,string)
re.sub(pat,repl,string)
re.compile(pat)

# 先頭と末尾の指定があるので「abc」の文字列だけにマッチ
re.search(r"^abc$","abc")
# abcdやxabcはマッチしない
print(re.search(r"^abc$","abcd"))
print(re.search(r"^abc$","xabc"))

# 任意のファイル拡張子を調べる
pat = r"\.png$"
re.search(pat,"abc.png")
# 末尾が.pngでなければマッチしない
print(re.search(pat,"abc.png-doc.txt"))

words = ["soy","soup","nuts","spot"]
pat = r"^s...$" # sから始まる4文字の文字列
[i for i in words if re.search(pat,i)]

# 繰り返し
re.search(r"ba*","b")
print(re.search(r"ba+","b"))
re.search(r"ba?","b")
re.search(r"ba*","baaaaaaa")
re.search(r"ba+","baaaaaaa")
re.search(r"ba?","baaaaaaa")
re.search(r"ba{3}","baaaaaaa")
re.search(r"ba{1,3}","baaaaaaa")
re.search(r"ba{3,}","baaaaaaa")

# 最小単位の繰り返し
s= "赤巻紙青巻紙黄巻紙"
re.findall(r".+紙",s)
re.findall(r".+?紙",s)

# 文字集合の指定[...]
zipre = re.compile(r"^[0-9]{3}\-[0-9]{4}$") # 正規表現パターンをコンパイル
zipre.search("440-0012")
print(zipre.search("4401-0012"))

# 単語の選択"|"
s = "I like red colour."
pat = r"\w+ (color|colour)"
re.search(pat,s)

# グループ(...)
s = "date:2019/10/15"
pat = r"(\d{4})/(\d{1,2})/(\d{1,2})"
g=re.search(pat,s)
g.groups()
