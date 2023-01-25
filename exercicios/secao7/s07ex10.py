'''
10 - Faça um programa para ler a nota da prova de 15 alunos e armazene em um vetor, calcule e imprima a media geral
'''

vetor = []
cont = media = soma = 0
while cont < 15:
    nota = int(input(f'informe a nota do {cont+1}° aluno: '))
    vetor.append(nota)
    cont += 1
print(vetor)
soma = sum(vetor)
media = soma/15
print(f'A media geral dos alunos é {media}')
