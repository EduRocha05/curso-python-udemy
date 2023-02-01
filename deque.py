'''
Modulos collections - Deque

O deque é uma lista de alta performance.

'''

#Fazendo import
from collections import deque

#Criando deque
deq = deque('geek')
print(deq)

#Adicionando elementos
deq.append('y')  #adiciona no final
print(deq)

deq.appendleft('k')  #adiciona no começo
print(deq)

#Removendo elementos
print(deq.pop())  #remove e retorna o ultimo elemento
print(deq)

print(deq.popleft())  #remove e retorna o primeiro elemento
print(deq)

