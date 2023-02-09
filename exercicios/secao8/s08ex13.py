"""
13. Faça uma função que receba a distancia em Km e quantidade de litros de gasolina consumidos por um carro em um
percurso, calcule o consumo em km/l e escreva uma mensagem
"""


def consumo_gasolina(distancia, litros):
    consumo = distancia/litros
    if consumo < 8:
        print(f'Venda o carro! Consumo de {consumo} Km/l')
    elif consumo > 14:
        print(f'Super Economico! Consumo de {consumo} Km/l')
    else:
        print(f'Economico! Consumo de {consumo} Km/l')


consumo_gasolina(8, 1)
