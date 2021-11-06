import re
fname = open('regex_sum_1218881.txt')
s = 0
for line in fname:
    z = re.findall('[0-9]+',line)
    for i in range(len(z)):
        try:
            x = float(z[i])
            s = s + x
        except:
            continue
print(s)
