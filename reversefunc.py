

def my_reverse(l):
    n=0
    a=[]
    while n <= (len(l)-1):
        a.append(l[len(l)-n-1])
        n+=1
    return a

