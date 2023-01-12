'''
42. Receba o salario-base de um funcionario. calcule e imprima o salario a receber, sabendo que esse funcionario
tem uma gratificação de 5% sobre o salario-base. alem disse, ele paga 7% de imposto sobre o salario-base.
'''

SalarioBase = float(input('Informe o salario base: '))

gratif = SalarioBase*(5/100)
imposto = SalarioBase*(7/100)

receber = (SalarioBase + gratif) - imposto
print(f'O valor a receber é de {receber}')
print(SalarioBase+gratif)
print(SalarioBase-imposto)


