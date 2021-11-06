fname = open('mbox-short.txt')
count = 0
for line in fname:
    if line.startswith('From '):
        count = count +1
        fg = line.split()
        print(fg[1])
print("There were", count, "lines in the file with From as the first word")
