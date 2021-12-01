'''
10. Write a Circle class with an instance variable named radius and a method named area. Create 
two more attributes named diameter and circumference and make them behave as read only attributes.
Perform data validation on radius, user should not be allowed to assign a negative value to it.
For a circle:
diameter =  2 * radius
circumference =  2 * 3.14 * radius
area =  3.14 * radius * radius
'''



class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2 * radius
        self.circumference = 2 * 3.14 * radius
        assert self.radius > 0, 'Radius cannot be negative'
    
    def __str__(self):
        return f'Circle with radius: {self.radius}'

    def area(self):
        return 3.14 * self.radius * self.radius


circle_1 = Circle(-10)
print(circle_1)
print(circle_1.area())
