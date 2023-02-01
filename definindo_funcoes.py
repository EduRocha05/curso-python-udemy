'''
Definindo Funções

São pequenas partes de codigo que realiza tarefas especificas;
Pode ou não receber entrada de dados e retornar uma saida;
São muito uteis para executar procedimentos similares por repetidas vezes;


OBS: Se escrever uma função que realiza varias tarefas dentro dela é bom fazer verificação para que a função seja
simplificada

ja utilizamos varios desde o inicio:
print()
len()
max()
min()
count()
etc.....
# Exemplo de utilização

cores = ['verde', 'amarelo', 'azul', 'branco']

# utilizando função integrada - (built-in) print()
print(cores)

# print(help(print))

# DRY - Dont Repaet Yourself

'''

'''
A forma de definir uma função:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde:
nome_da_funcao - sempre com letras minusculas e se for nome composto separado por underline(_)

parametros_de_entrada - são opcionais, tendo mais de um, cada um separada por virgula

bloco_da_funcao - tambem chamado de corpo ou implementação, é onde o processamento da funcao acontece, 
Neste bloco pode ter ou não retorno da função.

OBS: para definir um função utilizamos uma palavra reservada (def) informando ao python que estamos definindo uma 
função e abrimos o bloco de codigo com dois pontos(:)
'''

# definindo a primeira função

# Exemplo 1


def diz_oi():
    print('oi')


'''
Obs: 
1 - veja que dentro da nossas funções podemos utilizar outras funções
2 - veja que nossa função so executa uma tarefa ou seja a unica coisa que ela faz é dizer oi
3 - veja que esta função não recebe nenhum parametro de entrada 
4 - veja que esta função não retorna nada
'''

# utilizando funções
diz_oi()  # Atenção ao executar uma função adicionando parenteses

# Exemplo 2


def cantar_parabens():
    print('Parabens pra voce')
    print('Nesta data querida')
    print('.....')


# for n in range(4):
#    cantar_parabens()


# é possivel colocar a função dentro de uma variavel e executar - não é muito utilizado
canta = cantar_parabens
canta()
