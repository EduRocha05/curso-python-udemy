"""
Funções com Parametro (de entrada)

funções que recebem dados para serem processador dentro da mesma

# Refatorando uma função


def quadrado(num):
    # return num * num
    return num ** 2


print(quadrado(7))
print(quadrado(5))
print(quadrado(2))

# Refatorando a função


def cantar_parabens(aniversariante):
    print('Parabens pra voce')
    print('Nesta data querida')
    print('.....')
    print(f'Viva o {aniversariante}!!')


cantar_parabens('Eduardo')

OBS: Funções podem ter n paramentros de entrada, podemos receber quantos parametros forem necessarios
São separados por virgula


# Exemplo


def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 5))
print(multiplica(5, 2))
print(outra(3, 2, 'Python '))

# Obs: Se a gente informar um numero errado de parametro ou argumento teremos TypeError

# Nomeando parametros


def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('Eduardo', 'Rocha'))

# Diferença entre parametros e argumentos
# Parametros são variaves declaradas na definição de uma função
# Argumentos são dados passados durante a execução de uma função

# A ordem dos parametros importa

nome = 'Felicity'
sobrenome = 'Jones'
print(nome_completo(sobrenome, nome))

# Argumentos nomeados (Keyword Arguments)
# Caso utilizemos nomes dos parametros nos argumentos para informalos podemos utilizar qualquer ordem

print(nome_completo(nome='Eduardo', sobrenome='Rocha'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Marcia'))


"""

# Erro na utilização de return


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))
