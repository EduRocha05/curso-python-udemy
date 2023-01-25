'''
12 - Fazer um programa para ler 5 valores e em seguida mostrar a posição onde se encontra o maior de menor valor.
'''

vetor = []

maior = menor = soma = media = 0
posicao = 0
contador = 0
while contador < 5:
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
print(vetor)
print(f'O numero maior é {maior}')
print(f'o numero menor é {menor}')
print(f'A media dos valores do vetor é de {sum(vetor)/5}')
