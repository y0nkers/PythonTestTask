import math

class Shape: # Базовый класс фигуры
    def area(self):
        raise NotImplementedError("Производные классы должны реализовывать данный метод!")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # S = Pi * R^2
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, a, b, c):
        if not self._is_valid_triangle(a, b, c):
            raise ValueError("Треугольник с такими сторонами не существует")
        self.a = a
        self.b = b
        self.c = c

    def _is_valid_triangle(self, a, b, c):
        # Проверка неравенства треугольника
        return (a + b > c) and (a + c > b) and (b + c > a)

    def area(self):
        # s = sqrt(p * (p - a) * (p - b) * (p - c))
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def is_right_triangle(self):
        # a^2 + b^2 == c^2
        sides = sorted([self.a, self.b, self.c])
        return sides[0] > 0 and sides[0] * sides[0] + sides[1] * sides[1] == sides[2] * sides[2]
