cnt = 0

def set(n):
    global cnt
    cnt = n

def get():
    return cnt

def inc():
    global cnt  # globalがなければUnboundLocalError
    cnt += 1

def dec():
    global cnt  # globalがなければUnboundLocalError
    cnt -= 1


set(5)    
inc()
print(cnt)
dec()
print(cnt)
