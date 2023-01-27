'''
15 - Leia um vetor com 20 numeros inteiros. Escreva os elementos do vetor eliminando elementos repetidos
'''

vetor = []
cont = igual = numIgual = 0
while cont < 10:
    num = int(input('informe um numero: '))
    vetor.append(num)
    cont += 1
print()
for valor in vetor:
    if vetor.count(valor) >= 2:
        vetor.pop(valor)
print(vetor)
