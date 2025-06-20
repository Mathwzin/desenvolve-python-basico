#Desenvolva um programa que verifique se uma frase fornecida pelo usuário é um palíndromo (ou seja, lida da mesma forma de trás para frente). 
#Ignore espaços em branco ou sinais de pontuação, e considere maiúsculas e minúsculas da mesma forma. 
# Seu programa deve continuar rodando até que o usuário digite "Fim".
import string
while True:
    frase = input ("Digite uma frase (digite fim para encerrar): ")
    frase_minuscula = frase.lower()
    nova_frase = ""
    if frase == "fim":
        break
    frase_minuscula = frase_minuscula.replace(" ", "")
    for letra in frase_minuscula:
        if letra not in string.punctuation and letra != " ":
            nova_frase += letra
    if nova_frase == nova_frase[::-1]:
        print(frase, "é um palíndromo!")
    else:
        print(frase,"Não é um palíndromo.")
