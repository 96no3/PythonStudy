class Even:
    def __init__(self):
        self.i = 0    
    def __contains__(self,x):
        return x%2 == 0
    def __str__(self):
        return "even numbers"
    def __iter__(self):
        return self
    def __next__(self):
        result = self.i
        self.i += 2
        return result
    def __getitem__(self,i):
        return 2*i
    def __len__(self):
        return 0
        

2 in Even()
11 in Even()
2**100 in Even()

for x in Even():
    if x > 100:
        break

Even()[3]
Even()[900]

len(Even())

[*range(0,9,2)]
range(100,200,5)[3]
