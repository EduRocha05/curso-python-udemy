'''
Modulo Collections - Default Dict

Collections - High Performance Container Datatypes

#RECAP Dicionarios

dicionario = {'curso': 'Programação em Python'}
print(dicionario)
print(dicionario['curso'])
print(dicionario['outro']) #KeyError

Default Dict - ao criar um dicionario utilizando o default dict nos informamos um valor default
podendo utilizar um lambda para isso. Este valor sera utilizado sempre que não houver um valor definido.
Caso tentemos acessar a chave que não existe, essa chave sera criada e o valor default sera atribuido
'''

#Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python'
print(dicionario)
print(dicionario['outro'])
print(dicionario)
