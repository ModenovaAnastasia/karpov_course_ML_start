'''
В этом задании необходимо написать функцию check_string, которая сначала проверяет строку на наличие лишних символов пробела слева и справа. Если есть лишние пробелы, то тогда мы считаем строку неверной. Затем проверяет, что только первое слово начинается с большой буквы, а остальные с маленькой, и в конце проводит проверку, что последний символ является точкой.

def check_string(string):
    <...>
    return result
'''

def check_string(string):
  if string != string.strip():
    return False
  string = string.strip()
  if not string.endswith('.'):
    return False
  words = string[:-1].split()
  if not words:
    return False
  first = words[0]
  if not (
          (len(first) == 1 and first.isupper()) or
          (len(first) > 1 and first[0].isupper() and first[1:].islower())
  ):
    return False
  for word in words[1:]:
    if not word.islower():
      return False
  return True