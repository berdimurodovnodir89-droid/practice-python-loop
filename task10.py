n = int(input('n :'))

i =1 
while i < n + 1 :
    if  i % 3 == 0 and i % 5 == 0:
        print('FizzBusz')
    elif i % 3 == 0 :
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
else :
    print(n)

    i += 1 