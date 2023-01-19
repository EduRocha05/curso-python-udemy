''''
Listas

Listas em python funciona como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem dinamicos e tambem podermos colocar qualquer tipo de dado.

Dinamico: não possui tamanho fixo; ou seja podemos criar a lista e simplesmentes adicionando elementos;
Qualquer tipo de dado: não possuem tipo de dado fixo; ou seja; podemos colocar qualquer tipo de dado;

As listas em python são representadas por colchetes[]

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')

#podemos facilmente checar se determinado valor esta contido na lista
if 8 in lista4:
    print('Encontrei o numero 8')
else:
    print('Não encontrei o numero 8')

num = 7
if num in lista4:
    print(f'Encontrei o numero {num}')
else:
    print(f'Não encontrei o numero {num}')

#podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

#podemos facilmente contar o numero de ocorrencias de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

#adicionar elementos em listas
Para adicionar elementos utilizamos a função append
obs com append nos só conseguimos adicionar 1 elemento por vez

print(lista1)
lista1.append(42)
print(lista1)

lista1.append([8, 3, 1]) #coloca a lista como elemento unico(sublista
print(lista1)

lista1.extend([123, 44, 67]) #coloca cada elemento da lista como valor adicional a lista
print(lista1)

#podemos inserir um novo elemento na lista informando a posição do indice
#não substitui o valor inicial, o mesmo sera deslocado para a direita da lista
print(lista1)
lista1.insert(2, 'Novo valor')
print(lista1)

#podemos facilmente juntar duas listas
lista6 = lista1 + lista2
print(lista6)

lista1.extend(lista2)
print(lista1)

lista1 = lista1 + lista2

#podemos inverter uma lista
#forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)
#forma 2
print(lista1[::-1])
print(lista2[::-1])

#copiar uma lista
lista6 = lista2.copy()
print(lista6)

#podemos contar quantos elementos tem dentro da lista
print(len(lista5))

#podemos remover o ultimo elemento de um lista. o pop não somente remove mas tbm o retorna
print(lista5)
lista5.pop()
print(lista5)

#podemos remover um elemento pelo indice
#obs: os elementos a direita deste indice serão deslocados para a esquerda
#obs: se não houver elemento no indice informado teremos um erro
print(lista5)
lista5.pop(2)
print(lista5)

#podemos remover todos os elementos
print(lista5)
lista5.clear()
print(lista5)

#podemos repetir elementos em uma lista
nova = [1, 2, 3]
nova = nova * 3
print(nova)

#podemos converte uma string para uma lista
#ex1
curso = 'Programaçao em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)
#obs: por padrao o split separ os elemntos da lista pelo espaço entre elas.

#ex2
curso = 'Programaça,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

#convertendo uma lista em uma string
lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)

#pega uma lista e coloca espaço em cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

#pega uma lista e coloca o cifrao em cada elemento e transforma em uma string
curso = '$'.join(lista6)
print(curso)

#podemos colocar qualquer tipo de dado em uma lista inclusive misturando os dados
lista6 = [1, 2.34, True, 'Geek', [1, 2, 3], 4566465465456]

#iterando sobre listas
#ex01 - utilizando for

soma = ''
for elemento in lista2:
    print(elemento)
    soma += elemento
print(soma)

#ex02 - utilizando while
carrinho = []
produto = ''
while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

#utilizando variaveis em listas
numeros = [1, 2, 3, 4, 5]

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1, num2, num3, num4, num5]

#fazemos acesso ao elementos de forma indexada
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])
print()
#fazer acesso ao elementos de forma indexada inversa
print(cores[-1])
print(cores[-2])
print(cores[-3])
print(cores[-4])

for cor in cores:
    print(cor)

print()
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1


#gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

#listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)

#outros metodos
#encotrar o indice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]

#em qual indice esta o valor 6?
print(numeros.index(6))
#em qual indice esta o valor 9?
print(numeros.index(9))

#caso tenha esse elemento na lista sera apresentado erro
#print(numeros.index(19))

#numeros iguais retorna o indice do primeiro elemento encontrado
print(numeros.index(5))

#podemos fazer busca dentro de um range,ou seja, qual indice começar a buscar
print(numeros.index(5, 2)) #buscar 5 apartir do indice 2
#print(numeros.index(5, 4)) #buscar 5 apartir do indice 4 - caso tenha esse elemento na lista sera apresentado erro

#podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6)) #buscar 5 a partir do indice 3 ate o 6


#revisão slicing
#lista[inicio:fim:passo]
#range(inicio:fim:passo)

#trabalhando com slice de lista com o parametro inicio
lista = [1, 2, 3, 4]
print(lista[1:]) #iniciando no indice 1 e pegando todos os elementos restantes

#trabalhando com slice de lista com o parametro fim
print(lista[:2]) #pegando todos os elementos do inicio e finalizando no indice 2

#trabalhando com slice de lista com o parametro passo
print(lista[1::2]) #começa do indice 1 ate o fim e pulando de 2 em 2
print(lista[::2]) #pegando os elementos do inicio ate o fim e pulando de 2 em 2

#invertendo valores em uma lista
nomes = ['Geek', 'University']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)
nomes = ['Geek', 'University']
nomes.reverse()
print(nomes)

#soma, valor maximo, valor minimo, tamanho
#*se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]
print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

#transformar uma lista em tupla
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

#desempacotamento de listas
listas = [1, 2, 3]

num1, num2, num3 = listas

print(num1)
print(num2)
print(num3)

#copiando uma lista para outra(shallow copy e deep copy)
#forma 1 - deep copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)
nova.append(4)

print(lista)
print(nova)
#ao utilizar .copy copiamos os dados da lista para uma nova lista mas elas ficaram totalmente independentes
#modificando uma lista não altera a outra
#chamado de deep copy (copia profunda)

#forma 2 - shallow copy

lista = [1, 2, 3]
print(lista)

nova = lista
print(nova)
nova.append(4)

print(lista)
print(nova)
#ao utilizar a copia via atribuição e copiamos os dados para a nova lista mas apos modificar uma lista
#essa modificação se refletiu em ambas as listas
#chamado de shallow copy
'''




