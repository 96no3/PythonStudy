import functools as ft

(lambda a,b:a if a<b else b)

(lambda a,b:a if a<b else b)(3,5)
(lambda a,b:a if a<b else b)(5,3)

ft.reduce(lambda a,b:a if a<b else b,[1,10,2,-9,5,9])
ft.reduce(lambda a,b:a if a>b else b,[1,10,2,-9,5,9])

ft.reduce(lambda a,b:a and b,[True,True,True])
ft.reduce(lambda a,b:a and b,[True,True,False,True])
ft.reduce(lambda a,b:a or b,[True,True,False,True])
ft.reduce(lambda a,b:a or b,[False,False])
