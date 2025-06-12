#Solicite uma frase do usuário e usando compreensão de listas imprima:
# A lista de vogais da frase, ordenada alfabeticamente
# A lista de consoantes da frase (remova espaços em branco)
frase = input("Solicite uma frase do usuário e usando compreensão de listas imprima:")
vogais = [n for n in frase if n in 'aeiouAEIOU']
consoantes = [n for n in frase if not n in 'aeiouAEIOU']
print("Vogais:",vogais)
print ("Consoantes:",consoantes)