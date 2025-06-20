#3. Escreva um script que dado uma frase conta os espaços em branco.
frase = input ("Digite a frase:") 
espaços_em_branco = 0
for i in frase:
    if i == ' ':
        espaços_em_branco += 1 
print ("Espaços em branco: ", espaços_em_branco)
