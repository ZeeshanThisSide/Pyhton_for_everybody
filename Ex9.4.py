fname = open('mbox-short.txt')
fd = dict()
for line in fname:
    if line.startswith('From '):
        fs = line.split()
        fn = fs[1]
        fd[fn] = fd.get(fn,0)+1
a = None
b = None
c = fd.items()
for aa, bb in c:
    if a == None or bb > b:
        a = aa
        b = bb
print(a,b)
