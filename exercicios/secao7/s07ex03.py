
'''
03 - Ler um conjunto de numeros reais armazenando em vetor e calcular o quadrado dos componentes deste vetor
armazenando o resultado em outro vetor. os conjuntos tem 10 elementos cada.
'''

vetorA = [1.5, 6.8, 7.26, 24.6, 3.2, 5.2, 63.1, 8.8, 12.5, 4.7]
vetorB = []

indice = 0

while indice < len(vetorA):
    num = vetorA[indice]*vetorA[indice]
    vetorB.append(num)
    indice += 1
print(vetorB)
