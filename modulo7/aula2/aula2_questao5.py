#Implemente uma função chamada embaralhar_palavras() que recebe uma frase como entrada e retorna uma nova frase com as letras 
#internas de cada palavra embaralhadas. Mantenha sempre o primeiro e último caractere da palavra no lugar. 
#Dica: use a biblioteca random.
import random 
def embaralhar_palavras(frase):
    palavras = frase.split()
    nova_frase = ""
    for i in range(len(palavras)):
        palavra = palavras[i]
        if len(palavra) > 3:
            interna = list(palavra[1:-1])
            random.shuffle(interna)
            nova_palavra = palavra[0]
            for letra in interna:
                nova_palavra += letra
            nova_palavra += palavra[-1]
        else:
            nova_palavra = palavra
        nova_frase += nova_palavra
        if i < len(palavras) - 1:
            nova_frase += " "
    return nova_frase
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)