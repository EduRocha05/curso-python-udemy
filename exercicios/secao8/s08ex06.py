"""
6. Faça uma função que receba uma temperatura em celsius e retorne convertida em fahrenheit.
"""


def graus_fahrenheit(celsius):
    f = celsius * (9.0/5.0) + 32.0
    return f'a temperatura convertida é {f}ºF'


print(graus_fahrenheit(28))
