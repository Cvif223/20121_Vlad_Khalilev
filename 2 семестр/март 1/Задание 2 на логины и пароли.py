from string import ascii_lowercase


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw
    def render_template(self):
        return "\n".join(["<form action='#'>", self.login.get_html(), self.password.get_html(), '</form>'])


class TextInput:
    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text size={self.size}>"

    @classmethod
    def check_name(cls, name):
        if len(name) < 3 or len(name) > 50:
            raise ValueError("некорректное поле name")
        CHARS = "йцукенгшщзхъфывапролджэячсмитьбю " + ascii_lowercase
        CHARS_CORRECT = CHARS + CHARS.upper() + "1234567890"
        if any(x not in CHARS_CORRECT for x in name):
            raise ValueError("некорректное поле name")


class PasswordInput:
    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text size={self.size}>"

    @classmethod
    def check_name(cls, name):
        if len(name) < 3 or len(name) > 50:
            raise ValueError("некорректное поле name")
        CHARS = "йцукенгшщзхъфывапролджэячсмитьбю " + ascii_lowercase
        CHARS_CORRECT = CHARS + CHARS.upper() + "1234567890"
        if any(x not in CHARS_CORRECT for x in name):
            raise ValueError("некорректное поле name")

login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()

print(login)
print(html)