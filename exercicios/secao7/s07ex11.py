'''
11 - Faça um programa que preencha um vetor com 10 numeros reais calcule e mostre a quantidade de numeros negativos
e a soma dos numeros positivos desse vetor
'''

vetor = []
cont = negativos = positivos = soma = 0
while cont < 5:
    num = float(input(f'informe um valor: '))
    vetor.append(num)
    if num < 0:
        negativos += 1
    else:
        soma += num
    cont += 1
print(vetor)
print(f'A soma dos numeros positivos é de {soma}')
print(f'A quantidade de numeros negativos é de {negativos}')

