'''
Поэкспериментируем с арифметикой дат. Прибавьте к объекту даты, созданному ранее, 42 дня.
Для этого сложите  ваш объект даты с объектом timedelta из datetime. Запишите результат в переменную some_future.
'''
import datetime
launch_date = datetime.date(year=2022, month=2, day=10)
delta_1 = datetime.timedelta(days=42)
some_future = launch_date + delta_1
print(some_future)