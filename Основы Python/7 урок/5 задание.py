'''
Перепишите классы Triangle, Rectangle так, чтобы они наследовались от BaseFigure. Затем уберите реализацию всех методов и конструкторов в классах-потомках.
Есть ли у Triangle, Rectangle методы area, validate? Если есть, то что они возвращают при вызове?
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

class Rectangle(BaseFigure):
    n_dots = 4

tr = Triangle()
print(tr)
