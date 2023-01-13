'''
ranges

para trabalhar melhor com loops for

são utilizados para utilizar sequencias numericas não de for aleatoria mas sim de maneira especificada

forma geral

#Forma 1
range(valor_de_parada)
obs: valor de parada não incluido

for num in range(11):
    print(num)

#Forma 2
range(valor_inicial, valor_final)
obs: valor final não é incluido

for numero in range(1, 10):
    print(numero)

#forma 3
range(valor_inicial, valor_final, passo)
obs: valor final não é incluido, passo especificado pelo usuario

for num in range(1, 11, 2):
    print(num)

#forma 4 (inversa)
range(valor_inicial, valor_parada, passo)
obs: valor final não é incluido, passo especificado pelo usuario

for num in range(10, 0, -1):
    print(num)

'''

for num in range(10, 0, -1):
    print(num)
