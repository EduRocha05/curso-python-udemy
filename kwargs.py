"""
**Kwargs

o ** kwargs exige que utilizemos parametros nomeados e transforma esses parametros extras em dicionarios


# Exemplo


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa} é {cor}')


cores_favoritas(marcos='Verde', julia='Amarelo', fernando='Azul', vanessa='Branco')

# Obs: os parametros *args e **kwargs não sao obrigatorios.

cores_favoritas()
cores_favoritas(geek='navy')

# Exemplo 2


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Voce recebeu um cumprimento'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem vc é'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='OI'))
print(cumprimento_especial(geek='especial'))

# Nas nossas funções podemos ter (NESTA ORDEM):
# - Parametros obrigatorios
# - *args
# - Parametros default (não obrigatorios)
# - **kwargs

# Exemplo


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)
    print()


minha_funcao(8, 'julia')
minha_funcao(18, 'felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

# Função na ordem correta de parametros
# def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
#    return [a, b, args, instrutor, kwargs]


# Função com ordem incorreta de parametros
def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]



''''a = 1
b = 2
args = (3,)
instrutor = 'Geek'
kwargs = {'sobrenome': 'University', cargo='Instrutor'}''''


print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))


# Desempacotar com **kwargs

def mostra_nome(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Fernando', 'Sobrenome': 'Silva'}

# print(mostra_nome(nomes))  # TypeError
print(mostra_nome(**nomes))

"""


def soma_multiplos_numeros(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
tuplas = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tuplas)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)

# OBS: os nomes da chave em um dicionario devem ser os mesmo dos parametros da função

# dicionario = dict(d=1, e=2, f=3)  # TypeError
# soma_multiplos_numeros(**dicionario)

soma_multiplos_numeros(**dicionario, lang='Python')


