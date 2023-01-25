'''
05 - leia um vetor de 10 posições contar e escrever quantos pares ele possui.
'''

vetor = list(range(11))

cont = 0
for num in vetor:
    if num % 2 == 0:
        print(num, end=' ')
        cont += 1
print()
print(f'O vetor possui {cont-1} pares')

