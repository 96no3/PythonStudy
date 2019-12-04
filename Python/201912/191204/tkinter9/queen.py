#! usr/bin/env python

"""
           8 queens with symmetry operations of the board

 this program gives 
 12 distinct solutions by taking symmetry operations 
 such as rotations and reflections of the board into consideration
"""

### functions

def set_difference(a, b):
    return [x for x in a if not x in b]

def nreverse(ls):
    ls.reverse()
    return ls

def reverse(ls):
    return nreverse(ls[:])

def qmod (n):
    """function to determine the board color, 0 white 1, green"""
    return int((n / 8 - n % 8) % 2)

def queen_decode(c):
    """decode integer to list"""
    ls1=[]
    for i in range(8):
        ls1.append((c & 7) | (i << 3))
        c = c >> 3
    return ls1

def queen_encode(ls0):
    """encode list into integer"""
    c = 0
    for obj in ls0:
        c = (c << 3) | obj
    return c

### symmetry operations
def queen_usd(ls0):
    """up side down"""
    return [7 - o for o in ls0]

def queen_90(ls0):
    """rotating 90 degrees"""
    return nreverse([ls0.index(i) for i in range(8)])
      
def queen_180(ls0):
    """rotating 180 degrees"""
    return queen_90(queen_90(ls0))

def queen_270(ls0):
    """rotating 270 degrees"""
    return queen_90(queen_180(ls0))

def queen_dgla(ls0):
    """reflection on diagonal (1)"""
    return nreverse(queen_90(ls0))

def queen_dglb(ls0):
    """reflection on diagonal (2)"""
    return queen_usd(queen_90(ls0))

def queen_ok(col, qpos):
    """check if the queen's position is ok"""
    r = len(qpos)
    for i in range(r):
        c = qpos[i]
        j = r - i
        if c == col or col + j == c or col - j == c :
            return False
    return True

def queen_pos(qpos):
    """it retunrs possible queen positions"""
    return [c for c in range(8) if queen_ok(c, qpos)]

def eight_queens():
    """solving 8 queens taking symmetry operations into account"""
    
    def queen_sethash(ls0):
        """
        setting hash table
        'hash' is the hash table of the solution of the 8 queens
        if the key is a distinct solution the value is True, else False
        """
        
        c0 = queen_encode(ls0)
        if not (c0 in q_hash):
            for sop in (reverse, queen_usd, queen_90, queen_180, queen_270, queen_dgla, queen_dglb):
                q_hash[queen_encode(sop(ls0))] = False
            q_hash[c0] = True

    def queen(row, qpos):
        if row == 8:
            queen_sethash(qpos)
        else:
            for c in queen_pos(qpos):
                queen(1+row, qpos+[c])

    q_hash={}
    queen(0, [])
    return [queen_decode(key) for key, val in q_hash.items() if val]

if __name__=='__main__':
    for i, a in enumerate(eight_queens()):
        print('%2d: %s' % (i+1, a))
    
