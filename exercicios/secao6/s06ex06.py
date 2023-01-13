'''
06. Faça um programa que leia 10 numeros e leia sua media
'''

soma = 0
for cont in range(10):
    numero = int(input('Digite um numero: '))
    soma += numero
media = soma/10
print(soma)
print(media)
