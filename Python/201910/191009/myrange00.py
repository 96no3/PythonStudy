class MyRange():
    def __init__(self,*args):
        n_args = len(args)
        if n_args == 1:
            start,stop,step = 0,args[0],1
        elif n_args == 2:
            start,stop,step = args[0],args[1],1
        elif n_args == 3:
            [start,stop,step] = args
        else:
            raise Exception

        if not all([isinstance(x,int) for x in args]) or step == 0:
            raise ValueError

        if step > 0:
            in_range = lambda x: x < stop
        else:
            in_range = lambda x: x > stop

        cur = None

        def get_next():
            nonlocal cur
            if in_range(cur):
                result = cur
                cur += step
                return result
            else:
                raise StopIteration

        def initialize_iterator():
            nonlocal cur
            cur = start

        def get_value_by_index(i):
            result = start + step *i
            if not in_range(result):
                raise IndexError("MyRange: out of range")
            return result

        self.f = get_next
        self.i = initialize_iterator
        self.g = get_value_by_index

    def __iter__(self):
        self.i()
        return self

    def __next__(self):
        return self.f()

    def __getitem__(self,i):
        return self.g(i)
                
mr = MyRange(10,-2,-2)
for i in mr:
    print(i)
print([*MyRange(10,-2,-2)])
print("item:",mr[1])
