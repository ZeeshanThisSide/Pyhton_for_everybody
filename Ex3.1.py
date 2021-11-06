xx = input('Enter Hours: ')
yy = input('Enter your rate per hour: ')
x = float(xx)
y = float(yy)
if x <= 40:
    print(x*y)
else:
    print(40*y+(x-40)*(1.5*y))
