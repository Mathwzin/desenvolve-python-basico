#1 - Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura), bem como o preço do metro quadrado da região em ponto flutuante. 
# Calcule o valor do terreno e imprima o resultado como mostra o exemplo a seguir
# O terreno possui 250m2 e custa R$512,490.50
# Comente na linha acima de cada instrução uma breve descrição da instrução.

print ("Digite o comprimento do terreno:")
comprimento = int (input())
print ("Digite a largura do terreno:")
largura = int (input())
print ("Digite o preço do metro quadrado: ")
preco_m2 = float (input())
area_m2 = comprimento * largura
preco_total = preco_m2 * area_m2
print(f"A area do terreno é de {area_m2} m2 e custa R$ {preco_total:,.2f} ")