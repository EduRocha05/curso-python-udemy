'''
19. Faça um programa para verificar se um determinado numero inteiro é divisivel por 3 ou por 5 mas não simultaneamente
pelos dois
'''

num = int(input('Informe um numero: '))

if num % 3 == 0:
    print('O numero é divisivel por 3')
elif num % 5 == 0:
    print('O numero e divisivel por 5')
