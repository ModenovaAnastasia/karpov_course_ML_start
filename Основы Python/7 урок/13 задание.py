'''
Используя миксины из прошлого пункта, напишите класс JsonHandler, который будет наследоваться от классов ParsesBody и ParsesHeaders , иметь метод process() и конструктор, принимающий аргумент request и сохраняющий в self.request. В этом задании нужно использовать библиотеку json.

Метод process() должен работать следующим образом:

Если need_json() дает False, то возвращать None
Иначе получать тело через body(), пытаться считать его как json.loads(...) и возвращать число ключей в словаре. Если считать не удалось, то вернуть None.
Отправьте реализацию класса JsonHandler в LMS. Классы ParsesBody и ParsesHeaders отправлять не нужно.

Обратите внимание, что с помощью миксин функциональность проверки headers и получения body была вынесена за JsonHandler - наш класс сосредоточился именно на обработке.

# Пример использования
r = {'body': '{"a": 123, "b": 1234}',
     'headers': {'content-type': 'application/json'}
    }
print(JsonHandler(r).process())
'''

import json

class ParsesCookies:
    def cookies(self):
        return self.request.get("cookies", {})

    def is_authed(self):
        return "auth_key" in self.cookies()

class ParsesBody:
    def body(self):
        return self.request.get("body", "")

class ParsesHeaders:
    def headers(self):
        return self.request.get("headers", {})

    def need_json(self):
        return self.headers().get("content-type") == "application/json"

class BaseHandler:
    def __init__(self, request):
        self.request = request

class Handler(ParsesCookies, ParsesBody, ParsesHeaders, BaseHandler):
    pass

class JsonHandler(ParsesBody, ParsesHeaders):
    def __init__(self, request):
        self.request = request

    def process(self):
        if not self.need_json():
            return None
        try:
            data = json.loads(self.body())
            if isinstance(data, dict):
                return len(data)
            return None
        except json.JSONDecodeError:
            return None

r = {
    'body': '{"a": 123, "b": 1234}',
    'headers': {'content-type': 'application/json'}
}

print(JsonHandler(r).process())  # Выведет: 2
