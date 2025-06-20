#Implemente um código que leia uma string do usuário e imprima quantas vogais existem na frase e quais os seus índices da string.
# Dica: letra in "aeiou". Exemplo:
frase = input ("Digite a frase: ") 
vogais = 0 
indices = []
for i in range (len(frase)):
    if frase [i] in'aeiouAEIOU':
        vogais += 1
        indices.append(i)
print(vogais, "vogais") 
print("Índices", indices)