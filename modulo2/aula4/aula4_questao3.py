#3 - Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online. 
# O preço dos produtos é calculado multiplicando a quantidade pelo preço unitário. 
# Escreva um programa em Python que solicite do usuário o nome, o preço unitário e a quantidade de 3 produtos comprados e imprima ao final o preço total da compra.

print("Digite o nome do produto 1")
produto1 = input ()
print("Digite o preço do produto 1")
preco1 = float(input ())
print("Digite a quantidade do produto 1")
quantidade1 = int(input ())
print("Digite o nome do produto 2")
produto2 = input ()
print("Digite o preço do produto 2")
preco2 = float(input ())
print("Digite a quantidade do produto 2")
quantidade2 = int(input ())
print("Digite o nome do produto 3")
produto3 = input ()
print("Digite o preço do produto 3")
preco3 = float(input ())
print("Digite a quantidade do produto 3")
quantidade3 = int(input ())
valorTotal = (preco1* quantidade1) + (preco2* quantidade2) + (preco3* quantidade3)
print(f"Total: R${valorTotal:,.2f}")