'''
16 - Faça um programa que leia um vetor de 5 posições para numeros reais e depois um codigo inteiro. se o codigo for
zero finalize o programa, se for 1 mostre o vetor na ordem direta, se for 2 informe o vetor na ordem inversa.
Caso o codigo for diferente de 1 ou 2 escreva uma mensagem informando codigo invalido.
'''

vetor = []
cont = 0
cod = 5
while cont < 5:
    num = float(input('Informe um numero: '))
    vetor.append(num)
    cont += 1
while cod != 0:
    cod = int(input(''' Escolha a opção:
    [0] Sair
    [1] Ordem direta
    [2] Ordem Inversa
    '''))
    if cod == 1:
        print(vetor)
    elif cod == 2:
        vetor.reverse()
        print(vetor)
    elif cod == 0:
        print('Saindo...')
    else:
        print('Codigo invalido')
print('Fim')
