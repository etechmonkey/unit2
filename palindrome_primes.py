import math
l=[]
for i in range(10000,99999):
    d=2
    r=True
    while (d<math.sqrt(i)) & (r==True):
            if i%d==0:
                r=False
            else:
                r=True
            d+=1
    if (r==True) & (list(reversed(list(str(i))))==list(str(i))):
            l.append(i)

print(l)