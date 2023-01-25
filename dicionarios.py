'''
Dicionarios

Obs: em algumas linguagens de programação os dicionarios são conhecidos por Mapas

São coleções do tipo chave/valor

Dicionarios são representados por {}

print(type({}))

Obs: Chaves e valor são separados por ':' - 'chave':'valor';
tanto chave e valor podem ser de qualquer tipo de dado;
podemos misturar tipos de dados;


#Criação de dicionario - Forma 1 - mais comum
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

#Criação de dicionario - Forma 2 - menos comum
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

#Acessando elementos
#Forma 1 - acessando via chave (da mesma forma lista/tupla)
print(paises['br'])
print(paises['ru']) #caso tente acesso a uma chave que não existe teremos o KeyError

#Forma 2 - Acessando via get - recomendada
print(paises.get('br'))
print(paises.get('ru')) #caso tente acesso a uma chave que não existe imprime None

#podemos definir um valor padrão para caso não encontre o obejto com a chave informada
pais = paises.get('py', 'Não encontrado')
print(f'Encontrei o pais {pais}')

#Podemos verificar se determinada chave se encontra em um dicionario
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

#Podemos utilizar qualquer tipo de dado inclusive lista, tuplas como chaves de dicionarios

#Tuplas por exemplo são bastante utilizada como chaves de dicionarios, pois as mesmas são imutaveis
localidades = {
    (35.6895, 39.6917): 'Escritorio em Tokio',
    (40.7128, 74.0060): 'Escritorio em Nova York',
    (37.7749, 122.4194): 'Escritorio em São Paulo',
}

print(localidades)
print(type(localidades))

#Adicionando elementos em um dicionario

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

#forma 1 - mais comum
receita['abr'] = 350
print(receita)

#forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado) #receita.update({'mai': 500})
print(receita)

#Atualizando dados em um dicionario

#Forma 1
receita['mai'] = 550
print(receita)

#Forma 2
receita.update({'mai': 600})
print(receita)

#Conclusão1: a forma novos elementos ou atualizar dados em um dícionario
#Conclusão2: em dicionarios NÃO podemos ter chaves repetidas

#Remover dados
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

#Forma1 - mais comum
ret = receita.pop('mar')
print(ret)
print(receita)
#Obs1: aqui precisamos SEMPRE informar a chave e caso não encontre o elemento retorna KeyError
#Obs2: ao removermos um objeto, o valor do objeto é sempre retornardo.

#Forma2
del receita['fev']
print(receita)

del receita['fev']
#Obs: se a chave não existir sera gerado um KeyError.
#neste caso o valor removido não é retornado
'''

#imagine que vc tem um ecomerce, onde temos um carrinho de compra na qual adicionamos produtos.
'''
Carrinho de compra:
    Produto 1:
        nome:
        quantidade:
        preço:
    Produto 2:
        nome:
        quantidade:
        preço:
        

#1 - poderiamos utilizar uma lista para isso? Sim

carrinho = []
produto1 = ['Xbox360', 1, 2300.00]
produto2 = ['Halo', 1, 300.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
#Teriamos que saber qual é o indice de cada informação no produto.

# 2 - poderiamos utilizar um tupla para isso

produto1 = ('XboxOne', 1, 2300.00)
produto2 = ('Halo', 1, 300.00)

carrinho = (produto1, produto2)

print(carrinho)
#Teriamos que saber qual é o indice de cada informação no produto.

# 3 - poderiamos utilizar um dicionario para isso? sim

carrinho = []
produto1 = {'nome': 'XboxSeries', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'Gears', 'quantidade': 1, 'preco': 250.00}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
#desta forma, facilmente adicionamos e removemos produtos no carrinho e em cada produto
#podemos ter a certeza sobre cada informação

#Metodos de dicionarios
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

#Limpar o dicionario (zerar dados)
d.clear()
print(d)

#Copiando um dicionario para outro
#Forma 1 - Deep Copy

novo = d.copy() 
print(novo)

novo['d'] = 4
print(d)
print(novo)

#Forma 2 - Shallow Copy
novo = d
print(d)

novo['d'] = 4
print(d)
print(novo)

'''
#Forma não usual de criação de dicionarios

outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

#O metodo fromkeys recebe dois parametros: um iteravel e um valor.
#Ele vai gerar para cada valor iteravel um chave e ira atribuir a esta chave o valor informado

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)
