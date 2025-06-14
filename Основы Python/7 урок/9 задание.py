'''
Добавим могущества нашему вектору.
Добавьте методу красивый вывод при передаче его в print(...). Пример:
print(Vector([1, 2, 3]))
# Напечатает: "[1, 2, 3]" без кавычек

vec = Vector([1])
print(vec)
# Напечатает "[1]" без кавычек
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
    def __str__(self):
        return str(self.coords)
    def __repr__(self):
        return f"Vector({self.coords})"

print(Vector([1, 2, 3]))
vec = Vector([1])
print(vec)
