#for x in enumerate("abcde"):
#	print(x)

def valid(bits):
    n = len(bits)
    if n==0:
        return False
    #for x in bits:
    #    if x != "0" and x != "1":
    #        return False
    elif bits.count("0")+bits.count("1") != n:
        return False
    #else:
    #    return True
    return True

def test_exec():
    bits = input("Please input Binary number:")
    if bits.lower() == "exit":
        return False
    elif not valid(bits):
        print("Not available number:",bits)
        return False
    print("Decimal number:",convert(bits),"\n")
    return True

def convert(bs):
    #rbs=list(reversed(bs))
    n_decimal=0
    #for i in range(len(rbs)):
        #n_decimal += int(rbs[i])*2**i
    #for i,x in enumerate(rbs):
    for i,x in enumerate(reversed(bs)):
        n_decimal += int(x)*2**i
        print("Debug","i:",i,"x:",x,"result:",n_decimal)     
    return n_decimal    

def test():
    while test_exec():
        pass
    print("end")

#test_exec()
test()
