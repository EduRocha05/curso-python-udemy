from math import pi
"""
5. Faça uma função e um programa de teste para calculo de volume de uma esfera. sendo que o raio é passado por
parametro
"""


def teste_volume(raio):
    vol = 4/3 * pi * (raio ** 3)
    return vol


print(teste_volume(15))
