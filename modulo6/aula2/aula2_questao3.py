#Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50. 
# Crie uma terceira lista interseccao contendo apenas os valores que se repetem nas duas listas. Ao final imprima:
# Ambas as listas
# A lista intersecção ordenada
# A quantidade de vezes que cada elemento aparece em cada lista
# Atenção, a lista de intersecções não pode ter duplicatas.
import random
from collections import Counter
lista1 = []
lista2 = []
for n in range(20):
    elementos =  random.randint(0,50)
    lista1.append(elementos)
for n in range(20):
    elementos1 =  random.randint(0,50)
    lista2.append(elementos1)
interseccao = []
print("lista 1 - ",lista1)
print("lista 2 - ",lista2)
for elemento in lista1:
    if elemento in lista2 and elemento not in interseccao:
        interseccao.append(elemento )
interseccao.sort()
print("Interseccao - ", interseccao)
print("Cotagem ")  
for i in interseccao:
    print(f"{i}: lista1 = {lista1.count(i)}, lista2 = {lista2.count(i)}")
