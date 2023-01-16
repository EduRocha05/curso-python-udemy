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
'''

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')


