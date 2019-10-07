# リスト内包表記
[str(x) for x in range(10)]
[str(x**2) for x in range(10)]
[str(x) for x in range(10) if x%2==0]
[(x,y) for x in range(4) for y in ["a","b","c"]]
[(x,y) for x in range(4) for y in ["a","b","c"] if x%2==0]
