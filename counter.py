'''
Modulo Collections - Counter (contador)

Collections - High Performance Container Datatypes

Counter - rece um interavel como parametro e cria um objeto de tipo Collections Counter que é parecido
com um dicionario, contendo como chave o elemento da lista passada como parametro e como valor a quantidade de
ocorrencia desse elemento

#EXEMPLO 1

#Podemos utilizar qualquer iteravel, aqui temos uma lista
lista = [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

#Utilizando o counter
res = Counter(lista)
print(type(res))
print(res)
#Counter({1: 5, 2: 5, 3: 4, 4: 3, 5: 3, 45: 2, 66: 2, 43: 1, 34: 1})
#para cada elemento da lista o Counter criou uma chave e colocou como valor a quantidade de occorencias

#EXEMPLO 2
print(Counter('Geek University'))
#Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

'''
#Realizando Import
from collections import Counter

#EXEMPLO 3

texto = """ Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et 
dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""


palavras = texto.split()

#print(palavras)

res = Counter(palavras)
print(res)

#Encontrando as 5 palavras com mais ocorrencia no texto
print(res.most_common(5))

