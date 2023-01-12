'''
30. Leia um valor em real e a cotação do dolar. em seguida imprima o valor correspondente.
'''

real = float(input('Informe o valor em real: '))
dolar = float(input('Informe a cotação do dolar: '))

total = real/dolar

print(f'O valor total em dolares é {total:.2f}')
