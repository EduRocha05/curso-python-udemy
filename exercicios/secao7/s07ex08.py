'''
08 - Crie um programa que le 6 valores inteiros e em seguida mostre na tela os valores lidos na ordem inversa
'''

vetor = []

cont = 0

while cont < 6:
    num = int(input('Informe um numero inteiro: '))
    vetor.append(num)
    cont += 1
print(vetor)
print()
vetor.reverse()
print(vetor)
