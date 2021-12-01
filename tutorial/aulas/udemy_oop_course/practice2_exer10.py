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
        assert self.radius > 0, 'Radius cannot be negative'
    
    def __str__(self):
        return f'Circle with {self.radius} radius, {self.diameter} diameter and {self.circumference} circumference.'
    
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        assert new_radius > 0, 'Radius cannot be negative'
        self._radius = new_radius
        return self._radius

    @property
    def diameter(self):
        return 2 * self.radius

    @property
    def circumference(self):
        return 2 * 3.14 * self.radius

    def area(self):
        return 3.14 * self.radius * self.radius


circle_1 = Circle(10)
print(circle_1)
circle_1.radius = 70
print(circle_1)
