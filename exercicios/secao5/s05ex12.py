from math import log
'''
12. Ler um numero inteiro se o numero lido for negativo mensagem 'Numero invalido' se o numero for positivo calcular
logaritmo do numero
'''

num = float(input('Informe um numero: '))
if num > 0:
    print(f'O logaritmo do numero é {log(num):.4f}')
else:
    print('Numero Invalido')
