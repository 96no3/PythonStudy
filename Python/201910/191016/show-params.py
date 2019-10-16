#!/usr/bin/env python3

import cgi

# ヘッダ出力
print("Context-Type: text/html; charset=utf8mb4")
print("")

print("<pre>")
# URLパラメータを取得するFieldStorageオブジェクトを取得
# 辞書型と同じようにキーでアクセスしたり、keys()でパラメータの一覧を取得できる
form = cgi.FieldStorage()
"""
# formに"mode"が含まれるか？
if "mode" in form:
    print("mode=",form["mode"].value)
else:
    print("mode=空")
"""
# 特定のパラメータを取得して表示
mode = form.getvalue("mode",default="")
print("mode=",mode)

# すべてのパラメータを取得して表示
# getvalue()メソッド フォームのパラメータ値を取得 引数にキーを指定
print("---all params---")
for k in form.keys():
    print(k,"=",form.getvalue(k))
