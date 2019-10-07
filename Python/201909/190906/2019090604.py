def is_in(xs,container):
    for i in xs:
        if i in container:
            return True

a= ["a","b",0,-8]
b= [4,-9]
print(is_in(a,b))
