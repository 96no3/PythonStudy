def my_sort(xs):
    tmplist = xs.copy()
    n=len(tmplist)
    print(f"n={n}")
    for i in range(n-1):
        # フラグ管理し、入れ替えが起こらない＝ソートできているので処理を抜ける
        flag=False
        for j in range(1,n-i):
            print(f"i={i},j={j}")
            print(f"tmplist[j-1]={tmplist[j-1]},tmplist[j]={tmplist[j]}")
            if tmplist[j-1]>tmplist[j]:
                tmplist[j-1],tmplist[j]=tmplist[j],tmplist[j-1]
                flag = True
                print("入れ替えました",tmplist)
        if not flag:
            print("ソート済みです")
            break
    return tmplist

def my_sort2(xs):
    tmplist = xs.copy()
    n=len(tmplist)
    print(f"n={n}")
    for i in range(n-1):
        for j in range(n-i-1):
            print(f"i={i},j={j}")
            print(f"tmplist[j]={tmplist[j]},tmplist[j+1]={tmplist[j+1]}")
            if tmplist[j]>tmplist[j+1]:
                tmplist[j],tmplist[j+1]=tmplist[j+1],tmplist[j]
                print("入れ替えました",tmplist)
    return tmplist            
            

print(my_sort([1,3,-8,5,7,9,55,474]))
