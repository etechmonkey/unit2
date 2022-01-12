for n in range(1,1001):
    if((n%3==0) & (n%5==0)):
        a="FizzBuzz"
    elif(n%3==0):
        a="Fizz"
    elif(n%5==0):
        a="Buzz"
    else:
        a=n
    print(a)