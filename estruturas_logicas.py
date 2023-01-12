'''
Estruturas logicas
And (E), Or (ou), Not (não), is (é)

operadores unarios
 - not
operdores binarios
 - and, or, is

Para o AND, ambos os valores precisam ser True
Para o OR, um ou outro valor precisa ser True

Para o NOT, o valor booleano é invertido, se for true vira false e vice-versa
Para o IS, o valor é comparado com um segundo
'''
ativo = False
logado = False

'''if ativo or logado:
    print('Bem vindo usuario')
else:
    print('Voce precisa ativar a conta')'''

# se não estiver ativo faça isso
if not ativo:
    print('Voce precisa ativar a conta')
else:
    print('Bem vindo usuario')

print(not True)

'''if ativo is False:
    print('Voce precisa ativar a conta')
else:
    print('Bem vindo usuario')'''
