'''
14 - Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais e os escreva na tela.
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
        print(valor)
print(vetor)
