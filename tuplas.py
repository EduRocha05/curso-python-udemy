'''
tuplas (tuple)

são bastantes parecidas com listas
existem duas diferenças
1 - as tuplas são representadas por parenteses ()
2 - as tuplas são imutaveis, isso significa que ao criar uma tupla ela não muda
toda operação gera uma nova tupla

print(type(()))

#OBS 1: as tuplas são representadas por (), mas veja:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))
print()
tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))
print()
#OBS 2: as tuplas com 1 elemento:
tupla3 = (4) #não é uma tupla!
print(tupla3)
print(type(tupla3))
print()
tupla4 = (4,) #é uma tupla!
print(tupla4)
print(type(tupla4))
#CONCLUSÃO AS TUPLAS SÃO DEFINIDAS PELA VIRGULA E NÃO PELO PARENTESES

#podemos gerar uma tupla dinamicamente com range(inicio, fim, passo)
tupla = tuple(range(11))
print(tupla)

#desempacotamento de tupla
tupla = ('Geek University', 'Programação em Python: Essencial')

escola, curso = tupla

print(escola)
print(curso)
#gera erro se colocarmos um numero diferente de elementos para desempacotar

#OBS adição e remoção de elementos nas tuplas não existem dado o fato das tuplas serem imutaveis

#soma, valor max, valor min, tamanho
#se valores forem inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

#concatenação de tuplas
tupla1 = (1, 2, 3)
print(tupla1)
tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1+tupla2)
print(tupla1)
print(tupla2)

tupla3 = tupla1+tupla2
print(tupla3)

tupla1 = tupla1 + tupla2 #podemos sobscreever seus valores
print(tupla1)

#verificar se o elemento esta na tupla
tupla1 = (1, 2, 3)
print(3 in tupla1)

#iterando sobre um tupla
tupla1 = (1, 2, 3)
for n in tupla1:
    print(n)

for indice, valor in enumerate(tupla1):
    print(indice, valor)

#contando elementos dentro de uma tupla
tupla1 = ('a', 'b', 'c', 'd', 'a', 'b')
print(tupla1.count('a'))

escola = tuple('Geek University')
print(escola)
print(escola.count('e'))

#dicas na utilização de tuplas
#devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em um coleção
#exemplo1
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro')
print(meses)
#acesso a elementos de uma tupla tambem é semelhante a de uma lista
print(meses[5])
#iterar com while

i = 0
while i < len(meses):
    print(meses[i])
    i+=1

#verificamos em qual elemento esta na tupla
print(meses.index('Junho'))

#caso elemento não existe dara value erro

#slicing

#tupla[inicio:fim:passo]
print(meses[0:])
print(meses[5:])
print(meses[5:9])

#por que utilizar tuplas?

# Tuplas são mais rapidas do que listas
# Tuplas deixam seu codigo mais seguro, isso pq trabalhar com elementos imutavel traz segurança para o codigo

#copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla  #na tupla não temos problema de shallow copy

outra = (4, 5, 6)

nova += outra

print(nova)
print(tupla)
'''


