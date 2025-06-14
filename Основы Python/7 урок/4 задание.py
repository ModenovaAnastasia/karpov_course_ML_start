'''
Напишите класс BaseFigure, который имеет поле класса (т.е. на уровне класса) n_dots = None, метод area() "без реализации", метод validate() "без реализации".
Сделайте так, чтобы методы "без реализации" выбрасывали исключение NotImplementedError при их вызове и ничего другого не делали. Создайте также конструктор класса, который не принимает дополнительных аргументов и в реализации только лишь вызывает self.validate().
'''

class BaseFigure:
    n_dots = None
    def __init__(self):
        self.validate()
    def area(self):
        raise NotImplementedError
    def validate(self):
        raise NotImplementedError


