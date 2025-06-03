'''
В прошлом задании вы наверняка импортировали через import datetime, затем через точку обращались к нужным объектам. Это могло быть неудобно.
Используя синтаксис from ... import ..., сделайте следующий код рабочим:
datetime(month=3, day=8, year=2022) + timedelta(days=3, hours=5, minutes=6)
Обратите внимание на вызов datetime как функции внутри модуля.
Запишите  результат в переменную times
'''
from datetime import datetime, timedelta
times = datetime(month=3, day=8, year=2022) + timedelta(days=3, hours=5, minutes=6)
print(times)