'''
Возьмите классы Triangle и Rectangle из прошлого задания.
1. Переопределите метод area в каждом случае.
2. Переопределите конструктор в каждом случае (число аргументов тоже меняется). Не забудьте в конструкторе дочернего класса вызвать конструктор родительского класса!
3. Переопределите метод validate в каждом случае. Метод validate должен принимать только аргумент self и использовать созданные в конструкторе переменные. Для этого вы можете сначала сохранять в конструкторе входные данные в self.переменная, а затем вызывать конструктор суперкласса. Для Triangle данный метод должен проверять неравенство треугольника и выбрасывать ошибку ValueError("triangle inequality does not hold") либо возвращать значения сторон. Для Rectangle данный метод должен возвращать значения сторон.
В итоге вы получите два класса, которые построены по схожему шаблону. Этот общий шаблон был задан в классе BaseFigure. Создайте несколько объектов этих классов и попробуйте вызвать у них .area(), .validate(). Если вы пользуетесь IDE, то увидите интерактивные подсказки: она скажет, что такие методы есть и что эти методы перегружают (overload) методы из родительского класса. При этом вызов методов будет работать коррректно.
'''

import math
class BaseFigure:
    n_dots = None
    def __init__(self):
        self.validate()
    def area(self):
        raise NotImplementedError
    def validate(self):
        raise NotImplementedError

class Triangle(BaseFigure):
    n_dots = 3
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        super().__init__()
        self.p = (a + b + c)/2
    def area(self):
        return math.sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))
    def validate(self):
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            raise ValueError("triangle inequality does not hold")
        return self.a, self.b, self.c

class Rectangle(BaseFigure):
    n_dots = 4
    def __init__(self, a, b):
        self.a = a
        self.b = b
        super().__init__()
    def area(self):
        return self.a * self.b
    def validate(self):
        return self.a, self.b

tr = Triangle(3, 4, 5)
print(tr.area())
print(tr.validate())

rect = Rectangle(2, 7)
print(rect.area())

bad_tr = Triangle(1, 2, 8)
