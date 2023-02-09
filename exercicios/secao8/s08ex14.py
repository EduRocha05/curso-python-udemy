"""
14. Crie um programa que receba tres valores representando as medidas dos tres lados de um triangulo.
Elabore funções para determinar se eles formam um triangulo e determinar qual tipo de triangulo.
"""

# incompleta

def input_usuario():
    ladoa = float(input('Primeiro lado: '))
    ladob = float(input('Segundo lado: '))
    ladoc = float(input('Terceiro lado: '))
    return ladoa, ladob, ladoc


def forma_triangulo(ladoa, ladob, ladoc, triangulo=False):
    if ladoa > 0 and ladob > 0 and ladoc > 0:
        if ladoa < ladob + ladoc and ladob < ladoa + ladoc and ladoc < ladoa + ladob:
            print('Podem formar triangulo')
            triangulo = True
            return triangulo
        else:
            print('Não pode Formar triangulo')
    else:
        print('Informe numeros positivos')


def qual_tipo_triangulo(ladoa, ladob, ladoc):
    if ladoa == ladob == ladoc:
        print('Equilatero')
    elif ladoa != ladob and ladob != ladoc and ladoa != ladoc:
        print('Escaleno')
    else:
        print('Isosceles')


lados = input_usuario()

ret = forma_triangulo(*lados)

