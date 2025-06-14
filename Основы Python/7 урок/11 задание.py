'''
Добавьте в класс возможности сравнивать два вектора между собой и считать abs (это длина вектора, в Евклидовой метрике).

abs(Vector([-12, 5]))  # Должно быть 13

Vector([1, 3, 5]) == Vector([1])  # False
Vector([1, 3, 5]) == Vector([-1, 3, 5])  # False
Vector([1, 3, 5]) == Vector([1, 3, 5])  # True
'''

import math
class Vector:
    def __init__(self, coords):
        self.coords = coords
    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        if len(self.coords) != len(other.coords):
            raise ValueError(f"left and right lengths differ: {len(self.coords)} != {len(other.coords)}")
        new_coords = [a + b for a, b in zip(self.coords, other.coords)]
        return Vector(new_coords)
    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.coords) != len(other.coords):
                raise ValueError(f"left and right lengths differ: {len(self.coords)} != {len(other.coords)}")
            return sum(a * b for a, b in zip(self.coords, other.coords))
        elif isinstance(other, (int, float)):
            return Vector([a * other for a in self.coords])
        else:
            return NotImplemented
    def __rmul__(self, other):
        return self * other
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.coords == other.coords
    def __abs__(self):
        return math.sqrt(sum(a ** 2 for a in self.coords))
    def __str__(self):
        return str(self.coords)
    def __repr__(self):
        return f"Vector({self.coords})"

print(abs(Vector([-12, 5])))
print(Vector([1, 3, 5]) == Vector([1]))
print(Vector([1, 3, 5]) == Vector([-1, 3, 5]))
print(Vector([1, 3, 5]) == Vector([1, 3, 5]))
print(2 * Vector([1, 2]))

