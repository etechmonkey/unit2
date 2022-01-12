def big_fibonacci(n):
    x1=1
    x2=1
    while len(str(x2))<n:
        x2n = x1 + x2
        x1 = x2
        x2 = x2n
    return x2

print(big_fibonacci(1))
print(big_fibonacci(2))
print(big_fibonacci(3))
print(big_fibonacci(5))
print(big_fibonacci(30))
