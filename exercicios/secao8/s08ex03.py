"""
3. Faça uma função para verificar se um numero é positivo ou negativo. Sendo que o valor de retorno será 1 se positivo,
e -1 se negativo e 0 se for igual a 0.
"""


def verificar_numero(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0


print(verificar_numero(2598))
print(verificar_numero(158))
print(verificar_numero(-215))
print(verificar_numero(0))
