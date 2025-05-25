#Exercício de maratona:  https://www.beecrowd.com.br/judge/pt/problems/view/1094
# Maria precisa de sua ajuda para organizar os experimentos de seu laboratório. 
# Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada. 
# Este laboratório utiliza três tipos de cobaias: sapos, ratos e coelhos. 
# Entrada: A primeira linha de entrada é um inteiro N com a quantidade de experimentos registrados. 
# As N linhas seguintes contém um inteiro Quantia que representa a quantidade de cobaias utilizadas e um caractere Tipo ('S', 'R' ou 'C')
# com o tipo de cobaia (S:Sapo, R:Rato ou C:Coelho).
# Saída: Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia e o percentual de cada uma em relação ao total de cobaias utilizadas

n = int (input("Digite o numero total de cobais : "))
contador = 0 
rato = 0
sapo = 0
coelho = 0
while contador < n :
    quantia = int (input ("Digite a quantia "))
    tipo = str (input ("Digite o tipo de cobaia (S;Sapo, R:Rato, C: Coelho)"))  
    if tipo == 'S' or tipo == 's':
        contador +=1
        sapo +=quantia
    elif tipo == 'R' or tipo == 'r':
        contador +=1 
        rato += quantia
    elif tipo == 'C' or tipo == 'c':
        contador +=1 
        coelho +=quantia
    else :
        print ("Tipo de cobaia não compativel!")
print ("O número total de cobaia é de ", n)
print ("Total de sapos: ", sapo)
print ("Total de ratos: ", rato)
print ("Total de coelho: ", coelho)
per_ratos = 100 * rato / (sapo + rato + coelho)
per_sapos = 100 * sapo / (sapo + rato + coelho)
per_coelhos = 100 * coelho / (sapo + rato + coelho)
print (f"Percentual de Ratos: {per_ratos:,.2f} %")
print (f"Percentual de Sapos: {per_sapos:,.2f} %")
print (f"Percentual de Coelhos: {per_coelhos:,.2f} %")