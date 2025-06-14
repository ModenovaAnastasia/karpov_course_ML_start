'''
Напишите функцию sum_as_ints, которая принимает на вход список из строк, пытается привести их к целому числу через int(element) и считает сумму.
Список может содержать любые данные, но если они не приводятся через int(element), то программа должна их отбросить.
Вы можете попробовать выполнить int("hello"), int("3.14"), int("2,2") и увидеть, какие исключения выбрасывает программа. После этого можно обработать эти исключения у себя в функции.
'''

def sum_as_ints(str_list):
    total = 0
    for one_string in str_list:
        if one_string.isdigit():
            total += int(one_string)
        else:
            print(f"Can't be converted to int: {one_string}")
    return total