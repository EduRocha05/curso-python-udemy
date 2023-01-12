from math import sqrt
'''
02. Leia um numero fornecido pelo usuario. se esse numero for positivo calcule a raiz quadrada do numero.
Se for negativo mostre a mensagem dizendo que o numero é invalido
'''

num = int(input('Informe o numero: '))

if num > 0:
    raiz = sqrt(num)
    print(f'{raiz:.4f}')
else:
    print('Numero invalido')
