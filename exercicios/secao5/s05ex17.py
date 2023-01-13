'''
17. Faça um programa que calcule e mostre a area de um trapezio.
'''

base1 = float(input('Informe a base maior: '))
base2 = float(input('Informe a base menor: '))
alt = float(input('Informe a altura: '))

if base1 > 0 and base2 > 0:
    area = ((base1+base2)*alt)/2
    print(f'A area do trapezio é de {area:.2f} cm2')
else:
    print('Numeros invalidos')
