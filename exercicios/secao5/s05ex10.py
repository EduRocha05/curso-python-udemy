'''
10. Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal
utilizando as seguintes formulas
homens - (72.7*h)-58
mulheres - (62.1*h)-44,7
'''

h = float(input('Informe a altura: '))
sexo = input('Informe seu sexo: [M/F]: ')

if sexo in 'Mm':
    peso = (72.7*h)-58
    print(f'O peso ideal é {peso:.2f}')
else:
    peso = (62.1*h)-44.7
    print(f'O peso ideal é {peso:.2f}')

