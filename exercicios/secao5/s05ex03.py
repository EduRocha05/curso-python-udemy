from math import sqrt
'''
03. Leia um numero real. se o numero for positivo imprima a raiz quadrada. do contrario imprima o numero ao quadrado.
'''

num = float(input('Informe um numero: '))

if num > 0:
    raiz = sqrt(num)
    print(raiz)
else:
    quad = num**2
    print(quad)
