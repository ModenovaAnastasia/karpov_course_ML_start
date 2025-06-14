'''
Напишите классы ParsesCookies, ParsesBody, ParsesHeaders по условиям:

1. Класс ParsesCookies имеет метод cookies(), возвращающий все по ключу cookies из словаря self.request.
2. Класс ParsesCookies имеет метод is_authed(), который будет проверять, что в словаре cookies будет ключ auth_key (ни в коем случае не используйте такую авторизацию в реальных проектах).
3. Класс ParsesBody имеет метод body(), возвращающий текст по ключу body в self.request.
4. Класс ParsesHeaders имеет метод headers(), возвращающий все по ключу headers из словаря self.request.
5. Класс ParsesHeaders имеет метод need_json(), который возвращает True, если в headers по ключу "content-type" лежит значение "application/json", иначе False.
'''

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

request = {
    "cookies": {"auth_key": "123abc"},
    "body": "a long time ago, in a Galaxy far, far away",
    "headers": {"content-type": "application/json", "Accept": "application/json"}
}

handler = Handler(request)
print(handler.cookies())
print(handler.is_authed())
print(handler.body())
print(handler.headers())
print(handler.need_json())
