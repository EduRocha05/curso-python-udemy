"""
2. Faça uma função que receba a data atual(dia, mes, ano em inteiro) e exiba-a na tela no formato textual por extenso.
"""

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro')

for indice, nome in enumerate(meses):
    print(indice, nome)


def data_atual(dia, mes, ano):
    return f'{dia} de {mes} de {ano}'


print(data_atual(1, 1, 2000))

#incompleta