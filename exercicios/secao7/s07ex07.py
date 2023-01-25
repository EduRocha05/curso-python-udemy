'''
07 - Escreva um programa que leia 10 numeros inteiros e os armazene em um vetor. imprima o vetor o maior elemento e a
posição que ele se encontra
'''

vetor = []

cont = 0
while cont < 10:
    num = int(input('Informe um numero: '))
    vetor.append(num)
    cont += 1
print(vetor)
print(f'O maior elemento do vetor é o {max(vetor)}')
print(f'e esta localizado na posição {vetor.index(max(vetor))}')
