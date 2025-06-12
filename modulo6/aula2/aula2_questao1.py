#Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista. 
# Em seguida imprima na ordem estabelecida:
# A lista ordenada, sem modificar a lista original
# A lista original
# O índice do maior valor da lista
# O índice do menor valor da lista
import random
lista = []
valor = 0
for n in range (20):
    valor = random.randint(-100,100)
    lista.append(valor)
lista_ordenada = sorted(lista)
print(lista_ordenada)
print(lista)
print(max(lista))
print(min(lista))