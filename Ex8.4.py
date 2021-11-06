fh = open('romeo.txt')
lst = list()
for line in fh:
    fs = line.rstrip()
    fd = fs.split()
    for word in fd:
        if not word in lst:
            lst.append(word)
lst.sort()
print(lst)
