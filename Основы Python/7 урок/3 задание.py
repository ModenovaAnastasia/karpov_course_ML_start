'''
Создайте класс Rectangle (прямоугольник), который будет наследоваться от класса Triangle. Сделайте так, чтобы area(), конструктор и поле n_dots были верными. А именно:
1. Конструктор должен принимать 2 стороны: a, b
2. area() должен считать площадь как произведение смежных сторон: S=ab
3. Неравенство треугольника не нужно проверять.
4. n_dots должен быть объявлен на уровне класса и равняться 4.
'''

import math
class Triangle:
    n_dots = 3
    def __init__(self, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("triangle inequality does not hold")
        self.a = a
        self.b = b
        self.c = c
        self.p = (a + b + c)/2
    def area(self):
        return math.sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))

class Rectangle(Triangle):
    n_dots = 4
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b

rect = Rectangle(4, 5)
print(rect.area())
print(Rectangle.n_dots)
print(Triangle.n_dots)

