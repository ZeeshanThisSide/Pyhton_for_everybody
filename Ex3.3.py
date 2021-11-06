score = input('Enter score: ')
s = float(score)
if s > 1:
    print('Error, your score should be in the range of 0-1')
elif s >= 0.9:
    print('A')
elif s >= 0.8:
    print('B')
elif s >= 0.7:
    print('C')
elif s >= 0.6:
    print('D')
elif s >= 0:
    print('F')
elif s < 0:
    print('Error, your score should be in the range of 0-1')
