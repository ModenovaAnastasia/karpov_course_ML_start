'''
Напишите класс Vector, который на вход будет принимать список координат. Положите все координаты вектора в список self.coords.
Добейтесь того, чтобы объекты класса Vector можно было складывать через оператор + и получать на выходе тоже объект этого же класса.
Например:
# Будет работать
Vector([1, 2, 3]) + Vector([2, 3, 4]) # даст Vector([3, 5, 7])

# НЕ будет работать
Vector([1, 2]) + Vector([1, 2, 3])  # нельзя складывать векторы разной длины
# Должно возвращать ошибку (сообщение тоже!)
# ValueError: left and right lengths differ: 2 != 3
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
    def __repr__(self):
        return f"Vector({self.coords})"

v1 = Vector([1, 2, 3])
v2 = Vector([2, 3, 4])
print(v1 + v2)

v3 = Vector([1, 2])
v4 = Vector([1, 2, 3])
print(v3 + v4)

