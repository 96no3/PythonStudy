def show99(start=1,end=9):
    def join_delim(delim,strs):
        return delim + delim.join(strs) + delim
    def join_with_newline(delim,strs):
        d = delim + "\n"
        return d + d.join(s + "\n" for s in strs) + delim

    r= range(start,end+1)
    table99 = [[i*j for j in r] for i in r]
    widths = [len(str(x)) for x in table99[-1]]
    bar = join_delim("+",("-"*w for w in widths))
    rows = [join_delim("|",("%*d" %z for z in zip(widths,xs))) for xs in table99]

    result = join_with_newline(bar,rows)
    print(result)

show99()
