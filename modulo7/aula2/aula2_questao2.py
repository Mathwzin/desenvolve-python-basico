# Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".
frase = input("Digite uma frase: ")
frase_minuscula = frase.lower()
vogais = "aeiou"
for vogal in vogais:
    frase_minuscula = frase_minuscula.replace(vogal, "*")
print("Frase modificada: ",frase_minuscula)