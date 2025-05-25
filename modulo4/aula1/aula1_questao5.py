#Um instituto realizou uma pesquisa de público e precisa calcular a média de idade dos respondentes. 
# Escreva um programa que leia um inteiro N com a quantidade de respondentes e em seguida leia as N idades de cada respondente. Ao final, imprima a média das idades.
# (idade1 + idade2 + idade3 + … + idade_n)/N
n = int (input("Digite a quantidade de alunos: "))
soma = 0
contador = 0
while contador < n : 
    contador += 1
    idade = int (input ("Digite a idade:"))
    soma += idade
    media = soma / n
print ("A media é de :", media)