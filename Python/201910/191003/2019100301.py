def __next__(self):
    x=self.i
    if not x:
        self.i=3
        return 2
    primes = self.primes
    while True:
        found=True:
            for p,pp in primes:
                if x % p == 0:
                    found = False
                    break
                elif x < pp:
                    break
            if found:
                self.i = x + 2
                self.primes.append((x,x*x))
                return x
            x += 2
                
