'''
05. Faça um programa que peça ao usuario para digitar 10 valores e some-os
'''
soma = 0
for cont in range(10):
    numero = int(input('Digite um numero: '))
    soma += numero
print(soma)
