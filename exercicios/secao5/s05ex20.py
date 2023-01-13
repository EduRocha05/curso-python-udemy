'''
20. Dados 3 valores A B C verificar se eles podem ser valores dos lados de um triangulo e se forem,
se é triangulo escaleno, equilatero ou isosceles.
'''

ladoA = float(input('Primeiro lado: '))
ladoB = float(input('Segundo lado: '))
ladoC = float(input('Terceiro lado: '))

if ladoA < ladoB+ladoC and ladoB < ladoA+ladoC and ladoC < ladoA+ladoB:
    print('Podem formar triangulo')
    if ladoA == ladoB == ladoC:
        print('Equilatero')
    elif ladoA != ladoB and ladoB != ladoC and ladoA != ladoC:
        print('Escaleno')
    else:
        print('Isosceles')
else:
    print('Não podem formar triangulo')

