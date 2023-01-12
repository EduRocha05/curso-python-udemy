import math
'''
14. Leia um angulo em radianos e apresente-o convertido em graus.
'''

radiano = float(input('Angulo em Radianos: '))

graus = radiano * 180/math.pi

print(f'O angulo em graus é {graus:.0f}')

