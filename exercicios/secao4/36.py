from math import pi
'''
36. Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro.
'''

alt = float(input('Informe a altura: '))
raio = float(input('Informe o raio: '))

vol = 3.141592*(raio**2)*alt

print(f'O volume do cilindro é {vol:.2f}')
