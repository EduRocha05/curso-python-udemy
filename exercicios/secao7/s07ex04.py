'''
04 - Faça um programa que leia um vetor de 8 posições e em seguida leia tbm dois valores x e y quaisquer
correspondente a duas posições no vetor. ao final seu prgrama devera escrever a soma dos valores encontrados
nas respectivas posições x e y.
'''

vetor = []
indice = 0
soma = 0
while indice < 8:
    num = int(input('Informe um numero: '))
    vetor.append(num)
    indice += 1
print(vetor)

for num in vetor:
    soma = vetor[3]+vetor[5]

print(f'A soma dos valores do vetor nos indices 3 e 5 é : {soma}')
