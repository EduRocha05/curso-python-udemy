'''
MAPAS
conhecidos em python como dicionarios
dicionarios são representados por {}

receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)

#ITERAR SOBRE DICIONARIOS
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'{chave} : {receita[chave]}')

#ACESSANDO AS CHAVES
print(receita.keys())

for chave in receita.keys(): #chave
    print(receita[chave])

for valor in receita.values(): #valor
    print(valor)

#DESEMPACOTAMENTO DE DICIONARIOS
print(receita.items())

for chave, valor in receita.items():
    print(f'Chave = {chave} e valor = {valor}')

#Soma*, valor maximo*, valor minimo*, tamanho
#*se os valores forem todos inteiros ou reais
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

'''

receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)





