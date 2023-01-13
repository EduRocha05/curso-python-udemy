'''
02. Escreva um programa na tela de 1 ate 100, de 1 em 1, 3 vezes
for while
'''

cont = 0
while cont < 3:
    for num in range(1, 101):
        print(num, end='')
    print()
    cont += 1
