"""
List Comprehensions

Utilizando list comprehensions nos podemos gerar novas listas com dados processados a partir de outro iteravel

# Sintaxe

[ dado for dado in iteravel ]

# Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]
print(res)

Para entender melhor oq esta acontecendo devemos dividir a expressão em duas partes
1. for numero in numeros 
2. numero * 10


res = [numero / 2 for numero in numeros]
print(res)


def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]
print(res)


# List Comprehensions em Loop
# Loop
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

for numero in numeros:
    numeros_dobrados.append(numero * 2)

print(numeros_dobrados)


#list comprehension
print([numero * 2 for numero in numeros])
"""

# Outros Exemplos
# Ex1

nome = 'Geek University'
print([letra.upper() for letra in nome])

# Ex2


def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
print([caixa_alta(amigo) for amigo in amigos])

# Ex3

print([numero * 3 for numero in range(1, 10)])

# Ex4

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# Ex5

print([str(numero) for numero in [1, 2, 3, 4, 5]])
