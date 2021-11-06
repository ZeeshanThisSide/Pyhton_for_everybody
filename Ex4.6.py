def computepay(hrs, rate):
    h =float(hrs)
    r=float(rate)
    if h <= 40:
        return(h*r)
    elif h > 40:
        return((40*r)+((h-40)*(1.5*r)))
hrs = input('Enter Hours: ')
rate = input('Enter rate: ')
p = computepay(hrs, rate)
print('Pay',p)
