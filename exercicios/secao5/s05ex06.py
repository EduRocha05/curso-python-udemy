'''
06. Escreva um programa que dados dois numeros inteiros mostre na tela o maior deles assim como
a diferença entre ambos
'''

num1 = int(input('Informe o 1° numero: '))
num2 = int(input('Informe o 2° numero: '))

if num1 > num2:
    print(f'{num1} é o maior')
    dif = num1 - num2
    print(f'a diferença é de {dif}')
else:
    print(f'{num2} é o maior')
    dif = num2 - num1
    print(f'a diferença é de {dif}')

