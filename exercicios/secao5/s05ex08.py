'''
08. Faça um programa que leia 2 notas de um aluno verifique se as notas sao validas e exiba na tela a media
destas notas. uma nota valida deve ser obrigatoriamente um valor entre 0.0 e 10.0 onde caso a nota não possua valor
valido este fato dever ser informado ao usuario e o programa termina
'''

nota1 = float(input('Informa a 1 nota: '))
nota2 = float(input('Informa a 2 nota: '))

if 0.0 <= nota1 <= 10.0 and 0.0 <= nota2 <= 10.0:
    media = nota1+nota2/2
    print(f'A media é {media}')
else:
    print('Notas invalidas')
