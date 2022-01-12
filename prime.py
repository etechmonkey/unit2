def is_prime(n):
    d=2
    r=True
    if n<=1:
        return False
    else: 
        while (d<n) & (r==True):
            if n%d==0:
                r=False
            else:
                r=True
            d+=1
        return r
    

print(is_prime(17))
print(is_prime(5))
print(is_prime(12))
print(is_prime(1))
print(is_prime(97))

