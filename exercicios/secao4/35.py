from math import sqrt

'''
35. Sejam a e b catetos de um triangulo, onde a hipotenusa é obtida pela equação: ...
faça um programa que receba os valores de a e b e calcule o valorda hipotenusa atraves da equação
imprima o resultado dessa operação.
'''

a = float(input('Informe o valor do cateto A: '))
b = float(input('Informe o valor do cateto B: '))

hipo = sqrt((a**2)+(b**2))

print(f'O valor da hipotenusa é de {hipo}')

