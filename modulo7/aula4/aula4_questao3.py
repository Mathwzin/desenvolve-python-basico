#Baixe o arquivo contendo o roteiro do filme brasileiro "Estômago" e salve em seu computador com o nome "estomago.txt". 
#Em seguida crie um script em Python que abra o arquivo para leitura e imprima: 
#O texto das primeiras 25 linhas
#O número de linhas do arquivo
#A linha com maior número de caracteres
#O número de menções aos nomes dos personagens "Nonato" e "Íria" (inclua todas as variações de maiúsculas e minúsculas e atenção para não incluir a substring "iria" se ela fizer parte de outras palavras.
import string, os
with open ('estomago.txt','r', encoding='latin-1')as f:
    linhas = f.readlines()
for linha in linhas[:25]:
    print(linha.strip())
print(f"o arquivo tem {len(linhas)} linhas.")
maior = ''
for linha in linhas:
    if len(linha) > len(maior):
        maior = linha
print("A linha maior é: ", maior)
cont_nonato = 0
cont_iria = 0 
for linha in linhas:
    for palavra in linha.split():
        palavra_limpa = palavra.strip(string.punctuation).casefold()
        if palavra_limpa == 'nonato':
            cont_nonato = cont_nonato + 1
        if palavra_limpa == 'íria':
            cont_iria = cont_iria + 1
print(f"Nonato foi citado {cont_nonato} vezes.")
print(f"Ìria foi citada {cont_iria} vezes.")