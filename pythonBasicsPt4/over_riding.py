class Shape:
    def area(self):
        print("area not defined")

#circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
#rectangle class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

        def area(self):
            return self.length * self.width
        
#Triangle class
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    

c = Circle(5)
r = Rectangle(4, 6)
t = Triangle(3, 8)

print("Circle Area:", c.area())
print("Reactangle Area:", r.area())
print("Triangle Area:", t.area())