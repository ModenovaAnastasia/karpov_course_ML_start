'''
Вы заметили, что нам приходилось вставлять один и тот же код в несколько мест в прошлом задании?
Давайте избавимся от этого. Вынесите код печати массива в функцию print_array, затем поменяйте вашу исправленную реализацию math_task так, чтобы она использовала функцию print_array для печати массива. Ваш код в math_task станет меньше и не будет пестрить кучей строк с print.
Отправьте в LMS две функции: print_array и math_task.
Вызовите функцию math_task с данными test_data.
'''

def print_array(array):
    print("###")
    print(array)
    print("###")

def math_task(data):
    answer = []
    for elem in data:
        answer += [elem ** 3]
    print_array(answer)
    for i in range(len(answer)):
        answer[i] = answer[i] % 7
    print_array(answer)
    for i in range(len(answer)):
        answer[i] = answer[i] + data[i]
    print_array(answer)
    return answer


math_task(test_data)