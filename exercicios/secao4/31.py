'''
31. Leia um numero inteiro e imprima seu antecessor e seu sucessor.
'''

num = int(input('Informe o numero inteiro: '))

ant = num-1
suc = num+1

print(f'O sucessor do valor {num} é {suc}', end=' ')
print(f'e o antecessor é {ant}')