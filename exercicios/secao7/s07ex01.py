'''
01 - Faça um programa que possua um vetor denominado A
que armazene 6 números inteiros. O programa deve executar
os seguintes passos:

(a)Atribua os seguintes valores a este vetor: 1,0,5,-2,-5,-7.
(b)Armazene em uma variável inteira (simples) a soma entre os
valores das posições A[0],A[1] e A[5] do vetor e mostre na
tela esta soma.
(c)Modifique o vetor na posição 4, atribuindo a esta posição
o valor 100.
(d)Mostre na tela cada valor do vetor A, um em cada linha.
'''

soma = 0
vetorA = [1, 0, 5, -2, -5, 7]
print(f'O vetor A: {vetorA}')
soma = vetorA[0]+vetorA[1]+vetorA[5]
print(f'O resultado da soma das posições 0, 1 e 5 é: {soma}')
print()
for num in vetorA:
    print(num)
