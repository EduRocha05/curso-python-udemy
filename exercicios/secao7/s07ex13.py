'''
13 - Fazer um programa para ler 5 valores e em seguida mostrar a posição onde se encontra o menor e maior valor.
'''
vetor = []
cont = 0

while cont < 5:
    num = int(input('Infome um valor: '))
    vetor.append(num)
    cont += 1
print(f'O maior valor do vetor é {max(vetor)}', end=' ')
print(f'e sua posição é {vetor.index(max(vetor))}')
print(f'O menor valor do vetor é {min(vetor)}', end=' ')
print(f'e sua posição é {vetor.index(min(vetor))}')
