'''
14. A nota final de um estudante é calculada a partir de tres notas atribuidas entre o intervalo de 0 a 10,
respectivamente a um trabalho de laboratorio a uma avaliação semestral e a um exame final. a media das tres notas
mencionadas anteriormente obdece aos pesos: Trabalho de Lab: 2; Avaliação Semestral: 3; Exame final: 5. de acordo com o
resultado mostre na tela se o aluno esta reprovado(entre 0 e 2,9) de recuperação(entre 3 e 4,9) ou aprovado. faça todas
as verificações necessarias.
'''

nota1 = float(input('Informe a 1° nota: '))
nota2 = float(input('Informe a 2° nota: '))
nota3 = float(input('Informe a 3° nota: '))

media = ((nota1*2)+(nota2*3)+(nota3*5))/10
print(media)
if 0 < media < 2.9:
    print('Reprovado')
elif 3 < media < 4.9:
    print('Recuperação')
else:
    print('Aprovado')
