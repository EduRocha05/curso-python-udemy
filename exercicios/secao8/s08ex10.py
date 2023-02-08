"""
10. Elabore uma função que receba tres notas de um aluno como parametros e uma letra.
Se a letra for A, a função devera calcular a media aritmetica das notas do aluno; se for P devera calcular a media
ponderada com pesos 5, 3 e 2.
"""


def calculo_medias(aluno1, aluno2, aluno3, letra):
    if letra in 'Aa':
        media_a = (aluno1+aluno2+aluno3)/3
        return f'A media aritmetica das notas é de {media_a}'
    elif letra in 'Pp':
        media_p = ((aluno1*5)+(aluno2*3)+(aluno3*2))/10
        return f'A media ponderada das notas é de {media_p}'
    else:
        return 'letra invalida'


print(calculo_medias(7, 3, 5, 'a'))
