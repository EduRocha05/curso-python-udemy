"""
10. Faça uma função que receba dois números e retorne qual deles é maior.
"""


def num_maior(a, b):
    if a > b:
        return f'O valor {a} é o maior'
    else:
        return f'O valor {b} é o maior'


print(num_maior(15, 26))
