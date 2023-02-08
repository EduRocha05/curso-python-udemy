"""
8. Faça uma função que receba a altura e o raio de um cilindro circular e retorne o volume do cilindro.
"""


def volume_cilindro(alt, raio):
    vol = 3.141592 * (raio ** 2) * alt
    return f'O volume do cilindro é {vol:.2f}'


print(volume_cilindro(5, 4))
print(volume_cilindro(6, 5))
