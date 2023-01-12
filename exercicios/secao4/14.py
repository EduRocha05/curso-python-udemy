import math
'''
14. Leia um angulo em graus e apresente-o convertido em radianos.
'''

graus = float(input('Angulo em Graus: '))

radiano = graus * math.pi/180

print(f'O angulo em radianos é {radiano:.4f}')
