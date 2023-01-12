'''
41. Faça um programa que leia o valor da hora de trabalho em reais e numero de horas trabalhadas no mes
imprima o valor a ser pago ao funcionario, adicionado 10% sobre o valor calculado.
'''

ValorHora = float(input('Informe o valor da hora trabalhada: '))
NumHoras = int(input('Informe o numero de horas trabalhadas: '))

salario = ValorHora*NumHoras
porc = salario*(10/100)
print(f'O valor total a ser pago é de {salario+porc}')
