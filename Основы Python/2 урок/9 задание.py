'''
В этом задании Вам понадобится написать функцию find_substr,  которая принимает на вход два аргумента: подстроку (любой длины) и строку,
в которой нужно ее искать, и возвращает кортеж, представляющий собой пару [start, stop) первой позиции, где найдено слово.
'''
def find_substr(substring, string):
    start = string.find(substring)
    end = start + len(substring)
    return start, end