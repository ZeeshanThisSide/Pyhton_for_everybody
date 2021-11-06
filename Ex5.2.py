largest = None
smallest = None
while True:
    num = input('Enter a Number: ')
    if num == 'done':
        break
    try:
        n = float(num)
    except:
        print('Invalid input')
        continue
    if largest is None:
        largest = n
        smallest = n
    elif n < smallest:
        smallest = n
    elif n > largest:
        largest = n
print('Maximum is', largest)
print('Minimum is', smallest)
