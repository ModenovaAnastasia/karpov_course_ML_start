'''
Напишите реализацию reversed_, в которой не будет проблемы из прошлого пункта.
Оба варианта проверочного кода должны выдать Все хорошо.
Проверочный код:
if reversed_(reversed_([1, 2, 3])) == [1, 2, 3]:
    print("Все хорошо")
else:
    raise RuntimeError("Ошибка, после обращения дважды не получается исходный массив!")
----------
arr = [1, 2, 3]
if reversed_(reversed_(arr)) == arr:
    print("Все хорошо")
else:
    raise RuntimeError("Ошибка, после обращения дважды не получается исходный массив!")
'''

def reversed_(array):
    rv = []
    for i in range(len(array) - 1, -1, -1):
        rv.append(array[i])
    return rv