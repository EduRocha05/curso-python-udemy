from math import sqrt
'''
04. Faça um programa que leia um numero e, caso ele seja positivo calcule e mostre:
o numero digitado ao quadrado
a raiz quadrada do numero digitado
'''

num = int(input('Informe o numero: '))

if num > 0:
    print(num**2)
    print(sqrt(num))
else:
    print('Numero invalido')


