'''
Возьмите класс Triangle из предыдущего задания и добавьте метод area(), возвращающий площадь треугольника. Напомним, что при известных трех сторонах площадь треугольника можно подсчитать по формуле Герона.
Подумайте, как можно организовать код так, чтобы p считалась один раз.
Затем поменяйте конструктор: он должен проверять, что выполнено неравенство треугольника - каждая сторона меньше  суммы двух других. Если это условие не выполнено, выбрасывайте ValueError с текстом "triangle inequality does not hold" (передайте эту строку в конструктор ValueError).
Наконец, создайте два объекта данного класса с названиями tr_1 и tr_2 , в которых соблюдается неравенство треугольника. Также, сохраните в переменные square_1 и square_2 результаты вызовов методов .area() для объектов tr_1 и tr_2 соответственно.
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
tr_1 = Triangle(3, 4, 5)
tr_2 = Triangle(6, 7, 8)
square_1 = tr_1.area()
square_2 = tr_2.area()
print(square_1, square_2)