class Odd:
    def __init__(self):
        self.i = 1    
    def __contains__(self,x):
        return x%2 == 1
    def __str__(self):
        return "odd numbers"
    def __iter__(self):
        return self
    def __next__(self):
        result = self.i
        self.i += 2
        return result
    def __getitem__(self,i):
        return 2*i+1
    def __len__(self):
        return 0
        

2 in Odd()
11 in Odd()
3**100 in Odd()

for x in Odd():
    if x > 100:
        break

Odd()[3]
Odd()[900]

len(Odd())
