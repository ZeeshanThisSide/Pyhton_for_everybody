fname = open('mbox-short.txt')
fd = dict()
for line in fname:
    if line.startswith('From '):
        fs = line.split()
        fn = fs[5]
        fh = fn.split(':')
        fg = fh[0]
        fd[fg] = fd.get(fg,0)+1
lst = list()
c = fd.items()
for aa, bb in c:
    lst.append((aa,bb))
lst = sorted(lst)
for d,f in lst:
    print(d,f)
