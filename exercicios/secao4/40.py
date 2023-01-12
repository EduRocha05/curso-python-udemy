'''
40. Uma empresa contrata um encanador a R$30 por dia, faça um programa que solicite o numero de dias trabalhados
pelo encanador e imprima a quantia liquida que devera ser paga, sabendo que são descontados 8% para imposto de renda
'''

DiasTrabalhados = int(input('Informe o numero de dias trabalhados: '))
ValorDia = 30.00

salario = DiasTrabalhados * ValorDia
desc = salario*(8/100)

print(f'O salario é de {salario-desc}')
