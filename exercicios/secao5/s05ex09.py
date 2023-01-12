'''
09. Leia o salario de um trabalhador e o valor da prestação de um emprestimo se a prestação for maior de 20%
do salario imprima: 'emprestimo não concedido' caso contrario imprima: 'emprestimo concedido'
'''

salario = float(input('Informe o salario: '))
prestacao = float(input('Informe o valor da prestação: '))

porc = salario*(20/100)

if prestacao > porc:
    print('emprestimo não concedido')
    print(porc)
else:
    print('emprestimo concedido')
    print(porc)
