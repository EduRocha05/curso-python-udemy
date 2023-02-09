"""
Entendendo o *args

- o *args é um parametro, como outro qualquer. isso significa que voce podera chamar de qualquer coisa
desde que começe com *

- Exemplo:

*xis

mas por convenção utilizamos *args para defini-lo

o parametro *args é utilizado em uma função, coloca os valores extras informados como entrada em uma tupla

def soma_todos_numeros(*args):
    print(args)


print(soma_todos_numeros())

# Exemplo

def soma_todos_numeros(*args):
    '''total = 0
    for num in args:
        total = total + num
    return total'''
    return sum(args)


print(soma_todos_numeros(5, 5, 6, 6, 3, 7))

# Exemplo 2


def verifica_inf(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek'
    return 'Eu não tenho certeze quem vc é'


print(verifica_inf())
print(verifica_inf(1, True, 'University', 'Geek'))
print(verifica_inf(1, 'University', 3.145))
"""

# Exemplo


def soma_todos_numeros(*args):
    '''total = 0
    for num in args:
        total = total + num
    return total'''
    return sum(args)


print(soma_todos_numeros(5, 5, 6, 6, 3, 7))
print(soma_todos_numeros())

numeros = [1, 2, 3, 4, 5, 6]
#print(soma_todos_numeros(numeros))  # TypeError

# desempacotador

print(soma_todos_numeros(*numeros))

# OBS o asterisco serve para que informamos ao python passando uma coleção
