'''
06 - Faça um programa que receba do usuario um vetor com 10 posições. Em seguida devera ser impresso o maior
o menor elemento do vetor
'''

vetor = []

maior = menor = 0
posicao = 0
contador = 0
while contador < 10:
    num = int(input("Informe um numero: "))
    vetor.append(num)
    contador += 1
    if posicao == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    posicao += 1
print(f'O numero maior é {maior}')
print(f'o numero menor é {menor}')
print(vetor)



