'''
11. Escreva um programa que leia um numero inteiro maior do que zero e devolva na tela a soma de todos os numeros
por exemplo, o numero 251 correspondera o valor 8(2+5+1). se o numero lido não for maior que zero o programa terminara
com a mensagem 'numero invalido'
'''

num = int(input('Informe um numero: '))
soma = 0
if num > 0:
    soma += num % 10
    num = num/10
else:
    print('Numero invalido')
print(soma)

#incompleta