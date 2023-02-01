'''
Modulo Collections - Ordered Dict

#Em um dicionario, a ordem de inserção dos elemntos não é garantida
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave={chave} e valor={valor}')

OrderedDict - É um dicionario que nos garante a ordem de inserção dos elementos

# Fazendo import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave} e valor={valor}')
'''

# Entendendo a diferença entre Dict e Ordered Dict
# Dicionarios comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2)  # True - ja que a ordem dos elementos não importa para o dicionario

#Ordered Dict
from collections import OrderedDict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})
print(odict1 == odict2)  # False - ja que a ordem dos elementos importa para o Ordered Dict
