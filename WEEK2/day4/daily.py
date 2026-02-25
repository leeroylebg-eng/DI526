import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @property
    def diameter(self):
        return self.radius * 2

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter}, area={self.area()})"

    def __repr__(self):
        return f"Circle(radius={self.radius})"

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius


c1 = Circle(5)
c2 = Circle(10)
c3 = Circle.from_diameter(12)
c4 = Circle(3)

print(c1)
print(c2)
print(c1.area())
print(c1 + c2)
print(c1 > c2)
print(c1 == c4)

circles = [c2, c1, c3, c4]
print(sorted(circles))