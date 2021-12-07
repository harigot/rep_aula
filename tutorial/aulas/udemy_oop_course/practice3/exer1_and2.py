'''
1. This is a function to find the highest common factor of two numbers   
 def hcf(x,y):
        x=abs(x)
        y=abs(y)
        smaller = y if x>y else x
        s = smaller
        while s>0:
            if x%s==0 and y%s==0:
                break
            s-=1
        return s
Make it a static method in the Fraction class that you had written in earlier exercise


2. In your Fraction class, write a private instance method _reduce that reduces a fraction to its 
lowest terms. To reduce a Fraction to its lowest terms you have to divide the numerator and denominator 
by the highest common factor. Call this method in __init__and also call it on the resultant fraction 
in methods multiply and add.
'''



class Fraction:
    def __init__(self, nr, dr = 1):
        dr = self.indeterminacy_preventer(dr)
        if dr < 0:
            dr = -dr
            nr = -nr
        self.numerator = nr
        self.denominator = dr
        self._reduce()

    @staticmethod
    def hcf(x,y):
        x=abs(x)
        y=abs(y)
        smaller = y if x>y else x
        s = smaller
        while s>0:
            if x%s==0 and y%s==0:
                break
            s-=1
        return s

    def indeterminacy_preventer(self, dr):
        try:
            if dr == 0:
                print('The denominator cannot be 0.')
                raise ValueError
        except ValueError:
            print('invalid denominator, setting up for the default value.')
            return 1
        return dr

    def __str__(self):
        return f'{self.numerator} / {self.denominator}'

    def _reduce(self):
        hcf = self.hcf(self.numerator, self.denominator)
        if hcf == 0:
            return 
        self.numerator = self.numerator // hcf
        self.denominator = self.denominator // hcf
        return self

    def multiply(self, other):
        if isinstance(other, int):
            f = Fraction(self.numerator * other, self.denominator)
            return f._reduce()
        else:
            f = Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
            return f._reduce()
    
    def add(self, other):
        if isinstance(other, int):
            f = Fraction(self.numerator + other * self.denominator, self.denominator)
            return  f._reduce()
        else:
            f = Fraction((self.numerator * other.denominator) + (other.numerator * self.denominator), self.denominator * other.denominator)
            return f._reduce()


print(Fraction.hcf(8,47))
f1 = Fraction(6,36)
print(f1)
f2 = Fraction(2,-12)
print(f2)
f3 = f1.multiply(f2)
print(f3)
f3 = f1.add(f2)
print(f3)
f3 = f1.add(5) 
print(f3)
f3 = f1.multiply(5)
print(f3)
f3 = f1._reduce()
print(f3)