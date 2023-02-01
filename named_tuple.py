'''
Modulo Collections - Named Tuple

#REcap

tupla = (1, 2, 3)
print(tupla[1])

Named Tuple - São tuplas diferenciadas onde especificamos um nome para a mesma e tambem pararamentros


'''


# fazendo import
from collections import namedtuple

#definindo o nome e parametro
#Forma 1 - declaração

cachorro = namedtuple('cachorro', 'idade raca nome')

#Forma 2

cachorro = namedtuple('cachorro', 'idade, raca, nome')

#Forma 3

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

#Usando

ray = cachorro(idade=2, raca='chouchou', nome='Ray')
print(ray)

#Acessando os dados

#Forma 1
print(ray[0])  # idade
print(ray[1])  # raça
print(ray[2])  # nome

#Forma 2

print(ray.idade)
print(ray.raca)
print(ray.nome)


print(ray.index('chouchou'))
print(ray.count('chouchou'))


