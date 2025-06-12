#Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (com pelo menos 4 valores), 
# os armazena em uma lista e, usando fatiamento de listas, imprima:
# A lista original
# Os 3 primeiros elementos
# Os 2 últimos elementos
# A lista invertida (do fim para o começo)
# Os elementos de índice par (0, 2, 4 … )
# Os elementos de índice ímpar (1, 3, 5, … )
lista = []
while True:
    valor =  int (input("Digite pelo menos quatro valores para lista (0 para parar):"))
    if valor !=0:
        lista.append(valor)
    if valor == 0:
        break
print(lista)
print(lista[0:3])
print(lista[-2:])
print(lista[::-1])
pares = [i for i in lista if i % 2 ==0]
print (pares)
impares = [i for i in lista if i % 2 !=0]
print (impares)
