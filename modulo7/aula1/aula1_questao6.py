#Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. 
#Anagramas são palavras com os mesmos caracteres rearranjados.
from collections import Counter
frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")
anagramas = []
tamanho = len(palavra_objetivo)
contador_objetivo = Counter(palavra_objetivo)
for i in range(len(frase) - tamanho + 1):
    trecho = frase[i:i+tamanho]
    if Counter(trecho) == contador_objetivo:
        anagramas.append(trecho)
print("Anagramas: ", anagramas)