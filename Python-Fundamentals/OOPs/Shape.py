# Concept: Function Overriding

import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r * self.r

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(
            s * (s - self.a) * (s - self.b) * (s - self.c)
        )

c1 = Circle(5)
r1 = Rectangle(3, 5)
t1 = Triangle(4, 5, 6)

print(
    f"Area of circle: {c1.area()}\n"
    f"Area of rectangle: {r1.area()}\n"
    f"Area of triangle: {t1.area()}"
)