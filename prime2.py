def primes_below(n):
    l=[]
    for i in range(2,n):
        d=2
        r=True
        while (d<i) & (r==True):
            if i%d==0:
                r=False
            else:
                r=True
            d+=1
        if r==True:
            l.append(i)
    return l

print(primes_below(17))
print(primes_below(8))
print(primes_below(2))
