'''
10. Faça um programa que calcule e mostre a soma dos 50 primeiros pares
'''

soma = 0
for cont in range(50):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma += num
print(soma)
