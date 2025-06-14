'''
Продолжаем улучшать вектор. Добавьте в класс возможность умножать вектор на вектор и вектор на число. Не забудьте сохранять координаты вектора в self.coords.

Vector([1, 2, 3]) * Vector([2, 5, -2])  # даст 6
# 1 * 2 + 2 * 5 + 3 * (-2) = 6

Vector([1, 2]) * Vector([2, 3, 4])
# ValueError: left and right lengths differ: 2 != 3

Vector([2, 3, 5, 8]) * 5  # даст Vector([10, 15, 25, 40])
'''

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
    def __str__(self):
        return str(self.coords)
    def __repr__(self):
        return f"Vector({self.coords})"

print(Vector([1, 2, 3]) * Vector([2, 5, -2]))
print(Vector([2, 3, 5, 8]) * 5)
print(Vector([1, 2]) * Vector([2, 3, 4]))
