'''
Попробуем собрать совершенно новый класс, используя BaseFigure в качестве шаблона.
Напишите класс Circle, в котором в качестве n_dots будет float('inf'), area будет считаться как 3.14 * r^2, а конструктор будет принимать только один аргумент - r. Метод validate не должен принимать никаких аргументов и не должен осуществлять никаких проверок.
'''

class BaseFigure:
    n_dots = None
    def __init__(self):
        self.validate()
    def area(self):
        raise NotImplementedError
    def validate(self):
        raise NotImplementedError
class Circle(BaseFigure):
    n_dots = float('inf')
    def __init__(self, r):
        self.r = r
        super().__init__()
    def area(self):
        return 3.14 * self.r**2
    def validate(self):
        pass

c = Circle(3)
print(c.area())
print(c.n_dots)
