"""
12. Faça uma função que receba dois valores numericos e um simbolo. este simbolo representa a operação que se deseja
efetuar com os numeros. + adição - subtração / divisão * multiplicação.
"""


def calcular(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '/':
        return num1 / num2
    elif op == '*':
        return num1 * num2
    else:
        return 'Operação invalida'


print(calcular(5, 5, '+'))
print(calcular(5, 5, '-'))
print(calcular(5, 5, '/'))
print(calcular(5, 5, '*'))
print(calcular(5, 5, '~'))

