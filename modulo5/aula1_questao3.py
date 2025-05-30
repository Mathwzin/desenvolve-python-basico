#Escreva um programa em Python que utiliza a biblioteca random para gerar um número aleatório entre 1 e 10 e 
# peça ao usuário para adivinhar o número. 
# Forneça feedback se o palpite é muito alto, muito baixo ou correto. Interrompa a execução somente quando o usuário acertar o palpite.
import random 
n = (random.randint(1, 10))
while True:
    palpite = int (input("Digite seu palpite (Numero entre 1 e 10): "))
    if palpite == n:
        print ("Correto o número é ",n)
        break  
    elif palpite < n: 
        print ("Numero é maior que o seu palpite, tente novamente!")
    elif palpite> n:
        print ("O Número é menor que o seu palpite, tente novamente!")
