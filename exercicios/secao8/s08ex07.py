from math import sqrt
"""
7. Sejam a  e b os catetos de um triangulo, onde a hipotenusa é obtida pela equação: hip = raiz(a**2+b**2).
Faça uma função que receba os valores de a e b e calcule o valor da hipotenusa atraves da equação.
"""


def hipotenusa(a, b):
    hip = sqrt((a**2)+(b**2))
    return f'O valor da hipotenusa é de {hip:.2f}'


print(hipotenusa(5, 8))
