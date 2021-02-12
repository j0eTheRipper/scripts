from string import printable
from random import choice

printable = printable.replace(' ', '')
password = ''.join([choice(printable) for _ in range(14)])

print(password)
