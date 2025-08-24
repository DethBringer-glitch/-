import string
import random

simbols = list(string.ascii_letters + string.ascii_lowercase + string.octdigits + string.digits)
random.shuffle(simbols)
n = int(input('Введите количество символов:'))
password = ''.join(simbols[:n])
print(password)