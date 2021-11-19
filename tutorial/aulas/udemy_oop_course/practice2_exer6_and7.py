'''
6. Make a class Fraction that contains two instance variables, nr and dr (nr stands for numerator 
and dr for denominator). Define an __init__ method that provides values for these instance 
variables. Make the denominator optional by providing a default argument of 1.

In the __init__ method, make the denominator positive if it is negative. For example  -2/-3 should 
be changed to 2/3 and 2/-3 to -2/3.

Write a method named show that prints numerator, then '/' and then the denominator.


7. Define a method named multiply that multiples two Fraction instance objects. For multiplying two 
fractions, you have to multiply the numerator with numerator and denominator with the denominator.

Inside the method, create a new instance object that is the product of the two fractions and return 
it. Write your method in such a way that it supports multiplication of a Fraction by an integer also.

Similarly define a method named add to add two Fraction instance objects. Sum of two fractions 
n1/d1 and n2/d2 is (n1*d2 + n2*d1) / (d1*d2). This method should also support addition of a Fraction 
by an integer.

Test your fraction class with this code.

f1 = Fraction(2,3)
f1.show()
f2 = Fraction(3,4)
f2.show()
f3 = f1.multiply(f2)
f3.show()
f3 = f1.add(f2)
f3.show()
f3 = f1.add(5) 
f3.show()
f3 = f1.multiply(5) 
f3.show()
The output that you should get is given below.

2/3

3/4

6/12

17/12

17/3

10/3
'''



def indeterminacy_preventer(dr):
    while True:
        try:
            dr = int(dr)
            if dr == 0:
                print("The denominator cannot be 0.")
                raise ValueError
            break
        except ValueError:
            dr = input("Please enter a valid denominator: ")
    return dr


class Fraction:
    def __init__(self, nr, dr = 1):
        dr = indeterminacy_preventer(dr)
        if dr < 0:
            dr = -dr
            nr = -nr
        self.numerator = nr
        self.denominator = dr

    def show(self):
        print(self.numerator, "/", self.denominator)

    def multiply(self, other):
        if isinstance(other, int):
            return Fraction(self.numerator * other, self.denominator)
        else:
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
    
    def add(self, other):
        if isinstance(other, int):
            return Fraction(self.numerator + other * self.denominator, self.denominator)
        else:
            return Fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)


f1 = Fraction(2,3)
f1.show()
f2 = Fraction(3,4)
f2.show()
f3 = f1.multiply(f2)
f3.show()
f3 = f1.add(f2)
f3.show()
f3 = f1.add(5) 
f3.show()
f3 = f1.multiply(5) 
f3.show()
