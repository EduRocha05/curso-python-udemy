'''
17 - Leia um vetor de 10 posições e atribua valor 0 para todos os elementos que possuirem valores negativos
'''

vetor = []
cont = 0

while cont < 10:
    num = int(input('Informe um numero: '))
    vetor.append(num)
    cont += 1
print(vetor)

for indice, valor in enumerate(vetor):
    if valor < 0:
        vetor[indice] = 0
print(vetor)
