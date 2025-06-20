#Escreva um script que leia o arquivo salvo no exercício anterior e salva em um novo arquivo "palavras.txt", removendo todos os espaço
import os 
with open('arquivo.txt','r')as f:
    palavras = f.read()

palavras =[i+'\n'for i in palavras]
with open ('palavras.txt','w')as f:
    f.writelines(palavras)    