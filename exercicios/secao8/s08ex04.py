"""
4. Faça um função para verificar se um numero é um quadrado perfeito.
"""


def quadrado_perf(num):
    raiz = num ** (1/2)

    if (raiz ** 2) == num:
        return f' {num} é Quadrado Perfeito'
    else:
        return f' {num} não é quadrado perfeito'


print(quadrado_perf(1))  # é quad perfeito
print(quadrado_perf(2))
print(quadrado_perf(3))
print(quadrado_perf(9))  # é quad perfeito
print(quadrado_perf(16))  # é quad perfeito


