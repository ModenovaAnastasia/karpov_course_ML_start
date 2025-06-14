'''
В этом задании потребуется написать функцию process_string, которая приводит строку[1:] к нижнему регистру и заменяет все слова 'intern' на 'junior'.

def process_string(string):
    <...>
    return result

process_string('IIntern reads a lot of books')

Output:
'junior reads a lot of books'
'''

def process_string(string):
    processed = string[1:].lower()
    result = processed.replace('intern' ,'junior')
    return result