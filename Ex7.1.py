fname = input('Enter file name: ')
fh = open(fname)
for line in fh:
    z = line.upper()
    q = z.rstrip()
    print(q)
