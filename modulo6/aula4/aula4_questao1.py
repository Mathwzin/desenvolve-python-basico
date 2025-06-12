#Escreva um script python que use compreensão de listas para criar as seguintes listas:
# Todos os números pares entre 20 e 50, ou seja, [20, 22, 24, …, 48, 50]
# Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]
# Todos os números entre 1 e 100 que sejam divisíveis por 7
# Para todos os valores em range(0,30,3), escreva "par" ou "ímpar" dependendo da paridade do elemento (ex:['par', 'impar',… , 'impar'])
import random

lista_pares = [n for n in range (20,51)]
lista_quadrados = [1,2,3,4,5,6,7,8,9]
lista_1a100 = [n for n in range(1,101)]
lista_30  = [n for n in range (0,30,3)]
pares = [n for n in lista_pares if n % 2 == 0]
quadrado= [n**2 for n in lista_quadrados]
divisiveis_7 = [n for n in lista_1a100 if n % 7 == 0]
lista = ['par' if n %  2 == 0 else 'impar' for n in lista_30]
print(pares)
print(quadrado)
print(divisiveis_7)
print (lista)