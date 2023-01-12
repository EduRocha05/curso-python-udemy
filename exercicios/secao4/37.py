'''
37. Faça um programa que leia o valor de um produto e imprima o valor com desconto,
tendo em vista que o desconto foi de 12%
'''

valor = float(input('Informe o valor do produto: '))

desc = valor*(12/100)
total = valor-desc

print(f'O valor com desconto é {total}')
