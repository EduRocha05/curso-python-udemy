"""
Funções com retorno

numeros = [1, 2, 3]
ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno do print: {ret_pr}')

# Exemplo função


def quadrado_de_7():
    print(7*7)


ret = quadrado_de_7()
print(f'Retorno {ret}')

OBS: Quando uma função não retorna nuenhum valor, o retorno é None

# Refatorar a função para retornar o valor


def quadrado_de_7():
    return 7*7


ret = quadrado_de_7()
print(f'Retorno {ret}')

OBS: Funções em Python que retornam valores devem retornar estes valores com a palavra Return

OBS: Não precisamos necessariamente criar um variavel para receber o retorno de uma função
podemos passar a execução da função para outras funções.

# Refatorar a função para retornar o valor


def quadrado_de_7():
    return 7*7


# criamos uma variavel para receber o retorno da função
ret = quadrado_de_7()
print(f'Retorno {ret}')

print(f'Retorno: {quadrado_de_7() + 1}')

# Refatorando a primeira função


def diz_oi():
    return 'Oi!'


alguem = 'Pedro'
print(diz_oi() + alguem)


OBS: Sobre Return
1 - Ela finaliza a função
2 - Podemos ter em uma função diferentes returns
3 - Podemos em uma função retornar qualquer tipo de dado ate mesmo multiplos valores

# Exemplo 1 - Ela finaliza a função


def diz_oi():
    print('Estou sendo executado antes do return')
    return 'Oi! '
    print('Estou sendo executando apos o return') # nunca sera executado


print(diz_oi())

#Exemplo 2 - Podemos ter em uma função diferentes returns


def nova_funcao():
    var = False
    if var:
        return 4
    elif var is None:
        return 3.2
    return 'b'


print(nova_funcao())

# Exemplo 3 - Podemos em uma função retornar qualquer tipo de dado ate mesmo multiplos valores


def outra_funcao():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()

print(num1, num2, num3, num4)

# Vamos criar uma função para jogar moeda

from random import random


def joga_moeda():
    # Gera um numero pseudo randomico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())

# Erros comuns na utilização do retorno de uma função, codificação desnecessaria
# Colocar Else a mais sem necessidade

def eh_impar():
    num = 6
    if num % 2 != 0:
        return True
    return False


print(eh_impar())
"""


