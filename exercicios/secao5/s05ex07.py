'''
07. Faça um programa que recebe dois numeros e mostre o maior. se por acaso os dois numeros forem iguais
imprima a mensagem 'numeros iguais'
'''

num1 = int(input('Informe o 1° numero: '))
num2 = int(input('Informe o 2° numero: '))

if num1 > num2:
    print(f'{num1} é o maior')
elif num1 == num2:
    print('Numeros Iguais')
else:
    print(f'{num2} é o maior')
