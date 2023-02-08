"""
11. Escreva uma função que receba um numero inteiro maior que zero e retorne a soma de todos os seus algarismos.
Exemplo 251 corresponde ao valor 8 (2+5+1). Se o numero for menor que zero retorna "Numero invalido"
"""


def soma_alg(num):
    soma = 0
    if num >= 0:
        n = str(num)
        for i in range(len(n)):
            soma += int(n[i])
        return soma
    else:
        return 'Numero Invalido'


print(soma_alg(251))
print(soma_alg(123))
print(soma_alg(-2))
print(soma_alg(82532))
