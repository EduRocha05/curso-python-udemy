"""
List Comprehension

Nós podemos adicionar estruturas condicionais logicas
"""

# Ex1

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares)
print(impares)

# Refatorar

pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if numero % 2]
print(pares)
print(impares)

# Ex2

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)
