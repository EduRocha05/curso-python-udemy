'''
38. Leia o salario de um funcionario. Calcule e imprima o valor do novo salario,
sabendo que recebeu aumento de 25%.
'''

salario = float(input('Informe o salario: '))

porc = salario*(25/100)
aumento = salario+porc

print(f'O valor do salario com aumento é {aumento}')
