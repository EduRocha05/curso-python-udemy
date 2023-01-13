'''
15. Usando switch escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana
correspondente a este numero isto é domingo 1, segunda 2, etc...
'''

dia = int(input('Informe o dia: '))

match dia:
    case 1:
        print('Domingo')
    case 2:
        print('Segunda')
    case 3:
        print('Terça')
    case 4:
        print('Quarta')
    case 5:
        print('Quinta')
    case 6:
        print('Sexta')
    case 7:
        print('Sabado')
    case _:
        print('Invalido')
