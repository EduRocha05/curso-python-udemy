"""
Funções com parametro padrão  (default parameters)

- Funções onde a passagem de parametro seja opcional

# Exemplo de função onde a passagem de parametro seja opcional:

print('Geek University')
print()

# Exemplo de uma função onde a passagem de parametro seja obrigatoria:


def quadrado(num):
    return num ** 2

print(quadrado(7))
print(quadrado()) # TypeError


# Exemplo


def exponencial(num=4, potencia=2):
    return num ** potencia


print(exponencial(2, 3))
print(exponencial(3))  # por padrão eleve ao quadrado
print(exponencial(3, 5))  # eleva a potencia informada pelo usuario


# Obs: Se o usuario passar somente 1 argumento, este sera atribuido ao parametro numero
# e sera calculado o quadrado deste numero

# Obs: Se o usuario passar 2 argumentos o primeiro sera atribuido ao parametro numero e o segundo ao parametro potencia
# então sera calculado a potencia

print(exponencial())

# Erro: os parametros com valores default devem sempre estar ao final da declaração

def teste(num=2,potencia):
    return num ** potencia

print(teste(6)) # SyntaxError

# Outros Exemplos


def soma(num1=5, num2=3):
    return num1 + num2


print(soma(4, 3))
print(soma(4))  # Type Error
print(soma())  # Type Error

# Outro Exemplo


def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que voce era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))  # Coloca True como nome
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Stephany'))


# Por que utilizar parametros com valor padrao?
# Nos permite ser mais flexiveis nas funções
# Evita erros com parametros incorretos
# Nos permite trabalhar com exemplos mais legiveis de codigo

# Quais tipos de dados podemos utilizar como parametro: Numeros, Strings, Boolean, Listas, Tuplas, Funções, Etc....

# Exemplos

def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confusões
# Variaveis Globais
# Variaveis Locais

instrutor = 'Geek'  # Varivael Global


def diz_oi():
    instrutor = 'Python'  # Variavel Local
    return f'Oi {instrutor}'


print(diz_oi())

# OBS: se tivermos uma varival local com mesmo nome da variavel global, a local tera preferencia

def diz_oi():
    prof = 'Geek'
    return f'Olá {prof}'


print(diz_oi())
print(prof)  # NameError

# Atenção com variaveis globais - se puder evitar evite
# Exemplo 1

total = 0


def incrementa():
    total = total + 1  # UnboundLocalError (variavel local não esta inicializada)
    return total


print(incrementa())

# Exemplo 2

total = 0


def incrementa():
    global total  # avisando ao python que queremos utilizar a variaval global
    total = total + 1
    return total


print(incrementa())
print(incrementa())
print(incrementa())

# Podemos ter funções que são declaradas dentro de funções, e tambem tem uma forma especial de escopo de variavel


def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()


print(fora())
print(dentro())  # Não é reconhecido
"""


