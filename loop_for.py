'''
Estruturas de repetição
loop for

for item in iteravel:
    //execução do loop

utilizamos loops par iterar sobre sequencias ou sobre valores
strings
listas
range


#exemplo for 1
nome = 'Geek University'
lista =[1, 3, 5, 7, 9]
numeros = range(1, 10)

for letra in nome:
    print(letra)
#exemplo for 2
for num in lista:
    print(num)
#exemplo for 3

range(valor_inicial, valor_final)
obs: valor final não é incluido

for numero in range(1, 10):
    print(numero)


--
nome = 'Geek University'
lista =[1, 3, 5, 7, 9]
numeros = range(1, 10)
for i, v in enumerate(nome):
    print(nome[i])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)

--
qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma += num
print(f'A soma é {soma}')

-- imprimindo sem pular linha
nome = 'Geek University'
for letra in nome:
    print(letra, end='')

Emojis

Original - U+1F60D
modificado - U0001F60D

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)

'''

