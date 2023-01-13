'''
08. Escreva um programa que leia 10 numeros e escreva o menor valor lido e o maior valor lido.
'''

maior = 0
menor = 0
pos = 0
for cont in range(10):
    numero = int(input('Digite um numero: '))
    if pos == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    pos += 1
print(f'{maior} é o maior e {menor} o menor')


'''
if maior > menor:
            print(f'{numero} é o maior')
        if maior < menor:
            print(f'{numero} é o menor')
'''



