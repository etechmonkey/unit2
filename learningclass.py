class Rectangle():
    def __init__(self, l,w):
        self.length=l
        self.width=w
        self.area = l*w

    def scale(self, f):
        return Rectangle(f*self.length, f*self.width)

class Triangle():
    def __init__(self, a,b,c):
        self.length1=a
        self.length2=b
        self.length3=c
    def perimeter(self):
        return self.length1 + self.length2 + self.length3
    def area (self):
        import math
        s=Triangle(self.length1, self.length2, self.length3).perimeter()/2
        return math.sqrt(s*(s-self.length1)*(s-self.length2)*(s-self.length3))
    def scale(self,f):
        return Triangle(f*self.length1,f*self.length2, f*self.length3)
    def is_valid(self):
        if (self.length1<self.length2 + self.length3) & (self.length2<self.length1 + self.length3) & (self.length3< self.length1 + self.length2):
            return True
        else:
            return False
    def is_right(self):
        if (self.length1**2 == self.length2**2 + self.length3**2) or (self.length2**2 == self.length1**2 + self.length3**2) or (self.length3**2 == self.length2**2 + self.length1**2):
            return True
        else:
            return False  


