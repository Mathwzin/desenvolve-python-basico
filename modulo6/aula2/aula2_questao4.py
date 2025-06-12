#Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores. 
# Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. 
# Intercale os elementos até o final da primeira lista, adicionando ao final os elementos remanescentes da maior lista.
import random
lista1 = []
lista2 = []
repeticao = int (input("Digite a quantidade de elementos da lista 1:"))
print(f"Digite os {repeticao} elementos da lista 1:")
for n in range(repeticao):
    valor  =  int (input())
    lista1.append(valor)
repeticao = int (input("Digite a quantidade de elementos da lista 1:"))
print(f"Digite os {repeticao} elementos da lista 1:")
for n in range(repeticao):
    valor  =  int (input())
    lista2.append(valor)
tamanho1 = (len(lista1))
tamanho2 = (len(lista2))
if tamanho1 > tamanho2:
    lista_embaralhada = random.sample(lista2, len(lista2))
    lista_final = lista_embaralhada + lista1
    print("Lista intercalada:",lista_final)
if tamanho1 < tamanho2:
    lista_embaralhada = random.sample(lista1, len(lista1))
    lista_final = lista_embaralhada + lista2
    print("Lista intercalada:",lista_final)