import re

re.match("a","a")
re.match("a","b")
re.match("a","ab")

re.match("a+","a")
re.match("a+","aaaaaaaaaa")
re.match("a+","")

re.match("a*","")

re.match(".+","jjj")
re.match(".+","abghty")

re.match("[0123456789]","4")
re.match("[0-9]","a")
re.match("[0-9]+","457850")
re.match("[a-z]+[0-9]+","457850")
re.match("[a-z]+[0-9]+","dg457850")
re.match("[a-z]+[0-9]+","457yfh850")

re.match("\\++","+++++")
re.match(r"\++","+++++")
re.match(r"\\+","\\\\\\\\\\")

re.match(r"[a-zA-Z]+=[0-9]+","abc=30")
re.match(r"[a-zA-Z]+=[0-9]+","abc=xx")

obj=re.match(r"([a-zA-Z]+)=([0-9]+)","abc=30")
obj.groups()

matcher = re.compile(r"([a-zA-Z]+)=([0-9]+)")
matcher.match("abc=30")
matcher.match("abc=30").groups()