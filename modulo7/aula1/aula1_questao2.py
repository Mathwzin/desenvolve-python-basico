# 2.Escreva um programa que solicite ao usuário inserir seu primeiro nome e sobrenome separadamente. 
# Em seguida, concatene essas duas strings e exiba a mensagem de boas-vindas.
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
nome_sobrenome = nome + '' + sobrenome
print ("Boas vindas, ",nome_sobrenome,"!" )