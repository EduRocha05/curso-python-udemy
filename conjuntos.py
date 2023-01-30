'''
Conjuntos

- Conjuntos em qualquer linguagem de programação estamos fazendo referencia a teoria dos conjuntos da matematica.

- No python os conjuntos são chamados de Sets.
Da mesma forma que a matematica:
Sets não possuem valores duplicados
Sets não possuem valores ordenados
Elementos não são acessado via indice, ou seja, conjuntos não sõa indexados

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação
deles. Quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos (Sets) e Mapas (Dicionario) em Python:
    - Um dicionario tem chave/valor;
    - Um conjunto tem apenas valor;

    #DEFININDO UM CONJUNTO:
#forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) #Repare que temos valores repetidos
print(s)
print(type(s))
#OBS ao criar um conjunto caso seja adicionado um valor ja adicionado o mesmo sera ignorado sem gerar erros

#forma 2 - mais comum
s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

#PODEMOS VERIFICAR SE O ELEMENTO ESTA CONTIDO NO CONJUNTO
if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

#importante lembrar que alem de não ter valores duplicados, não temos ordem

lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista}') #Aceita valores duplicados

tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(f'tupla: {tupla}') #Aceita valores duplicados

dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionario: {dicionario}') #Não aceita valores duplicados

conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto}') #Não ceita valores duplicados

# assim como t odo outro conjunto de daodos podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 35.22, 44}
print(s)
print(type(s))

# podemos iterar em um set normalemnte
for valor in s:
    print(valor)

#USOs interessante com sets

#Imagine um formulario de visitantes
#informam manualmente a cidade de onde vieram
#adicionamos as cidades em uma lista python, ja que uma lista pode adicionar mais elementos e ter repetição

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', ' São Paulo', 'Cuiaba']
print(cidades)
print(len(cidades))

#Agora precisamos saber quantas cidades diferentes, ou seja, unicas temos.
#Podemos utilizar o SET

print(len(set(cidades)))

# Adicionando elementos em um conjunto
s = {1, 2, 3}
s.add(4)
s.add(4)  # não adiciona, ignorado e não gera erro
print(s)

# Removendo elementos em um conjunto
s = {1, 2, 3}
print(s)

#forma 1 - informa o valor a ser removido
s.remove(3)
print(s)
#s.remove(33)  #caso o valor não seja encontrado sera gerado um KeyError
#OBS: nenhum é retornado

#forma 2
s.discard(2)
print(s)
#s.discard(22)  #caso o valor não seja encontrado não sera gerado erro

#Copiando um conjunto para outro
s = {1, 2, 3}
print(s)

#Forma1 - deep copy
novo = s.copy()
print(novo)
novo.add(4)

print(novo)
print(s)

#Forma2 - shallow copy
novo = s
novo.add(4)
print(novo)
print(s)

#Podemos remover todos os itens de um conjunto
s.clear()
print(s)

#Metodos matematicos de conjuntos
#Imagine que temos dois conjuntos: um com estudantes de python e outro com estudandes de java

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

#veja que possui alunos repetidos
#precisamos gerar um conjunto com estudantes unicos

#Forma 1 - Utilizando union
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

#Forma2 - utilizando o caracter |
unicos2 = estudantes_python | estudantes_java
print(unicos2)

#Gerar um conjunto de estudantes que estão em ambos os cursos

#Forma 1 - Utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

#Forma 2 - Utilizando o &
ambos2 = estudantes_python & estudantes_java
print(ambos2)

#Gerar um conjunto de estudantes de um curso que não estão no outro

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

#Soma*, Valor Maximo*, Valor Minimo*, Tamanho
#Se os valores forem inteiro e real

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
'''



