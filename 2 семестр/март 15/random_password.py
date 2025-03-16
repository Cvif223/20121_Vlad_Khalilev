from random import randint
class RandomPassword:
    def __init__(self, psw_chars, min_lenght, max_lenght):
        self.psw_chars = psw_chars
        self.min_lenght = min_lenght
        self.max_lenght = max_lenght
    def __call__(self, *args, **kwargs):
        password = ""
        psw_len = randint(min_length, max_length)
        for _ in range(psw_len):
            char = psw_chars[randint(0, len(self.psw_chars)) - 1]
            password += char
        return password

min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjk1zxcvbnm0123456789!@#$%&*"
rnd = RandomPassword(psw_chars, min_length, max_length)
psw = rnd()
print(psw)
psw = rnd()
print(psw)