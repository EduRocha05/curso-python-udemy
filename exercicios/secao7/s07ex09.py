'''
09 - Crie um programa que le 6 valores inteiros pares e em seguida mostre na tela os valores lidos na ordem inversa
'''

vetor = []
cont = 0

while cont < 6:
    num = int(input('Informe um valor inteiro par: '))
    if num % 2 == 0:
        vetor.append(num)
        cont += 1
    else:
        print('Numero invalido')
print(vetor)
print()
vetor.reverse()
print(vetor)
