'''
13. Faça um algortimo que calcule a media ponderada das notas de 3 provas. a primeira e a segunda prova tem peso 1 e
a terceira tem peso 2 ao final mostrar a media do aluno e indicar se o aluno foi aprovado ou não. a nota para aprovação
tem que ser igual ou superior a 60 pontos
'''

nota1 = float(input('Informe a 1° nota: '))
nota2 = float(input('Informe a 2° nota: '))
nota3 = float(input('Informe a 3° nota: '))

media = ((nota1*1)+(nota2*1)+(nota3*2))/4
print(media)
if media > 60:
    print('Aprovado')
else:
    print('Reprovado')
