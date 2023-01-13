'''
07. Faça um programa que leia 10 inteiros positivos ignorando os não positivos imprima a media
'''
soma = 0
pos = 0
for cont in range(10):
    numero = int(input('Digite um numero: '))
    if numero > 0:
        soma += numero
        pos += 1
media = soma/pos
print(soma)
print(media)
