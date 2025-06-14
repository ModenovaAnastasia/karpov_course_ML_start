'''
Используя миксины из прошлого пункта, напишите класс SecureTextHandler, который будет наследоваться от классов ParsesBody и ParsesCookies , иметь метод process() и конструктор, принимающий один аргумент и сохраняющий его в нужное поле класса.
Метод process() должен работать следующим образом:
1.Если is_authed() дает False, то возвращать None.
2. Иначе получать тело через body() и возвращать его длину.
Добейтесь работоспособности на примере и реализацию класса SecureTextHandler отправьте в LMS. Классы ParsesBody и ParsesHeaders, ParsesCookie отправлять не нужно.
# Примеры
r = {'cookies': {'auth_key': '123'},
     'body': 'hello'
    }
print(SecureTextHandler(r).process())
# 5
r = {'cookies': {},
     'body': 'hello'
    }
print(SecureTextHandler(r).process())
# None
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


class SecureTextHandler(ParsesBody, ParsesCookies):
    def __init__(self, request):
        self.request = request

    def process(self):
        if not self.is_authed():
            return None
        return len(self.body())


r = {'cookies': {'auth_key': '123'}, 'body': 'hello'}
print(SecureTextHandler(r).process())

r = {'cookies': {}, 'body': 'hello'}
print(SecureTextHandler(r).process())
