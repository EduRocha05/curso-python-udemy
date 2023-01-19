'''
02 - Crie um programa que le 6 valores inteiros e em seguida mostre na tela os valores lidos
'''

indice = 0
vetor = []
while indice < 6:
    num = input('Informe o numero para adicionar: ')
    vetor.append(num)
    indice += 1
print(vetor)
