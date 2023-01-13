'''
18. Faça um programa que mostre ao usuario um menu com 4 opções de operações matematicas. o usuario escolhe uma das
opções e seu programa então pede dois valores numericos e realiza a operação mostrando o resultado e saindo.
'''

opc = input('Informe a operação desejada [+ - / *]: ')
num1 = int(input('Informe um numero: '))
num2 = int(input('Informe outro numero: '))

match opc:
    case '+':
        print(f'A soma é = {num1+num2}')
    case '-':
        print(f'A subtração é = {num1-num2}')
    case '*':
        print(f'A multiplicação é = {num1*num2}')
    case '/':
        print(f'A divisão é = {num1/num2}')
    case _:
        print('Invalido')
