fname = input('Enter file name: ')
fh = open(fname)
count = 0
s = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        x = line.lstrip("X-DSPAM-Confidence:")
        y = float(x)
        s = s + y
        count = count + 1
print('Average spam confidence:', s/count)
