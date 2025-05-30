#Desenvolva um programa em Python que peça ao usuário para inserir dois números decimais e calcule a diferença absoluta entre esses dois números. 
# Utilize a função nativa abs para garantir que o resultado seja sempre positivo e round para arredondar o resultado para duas casas decimais.

n1 = float (input("Digite o primeiro número: "))
n2 = float (input("Digite o segundo número: "))
diferenca = abs (n1 - n2 )
diferenca = round(diferenca, 2)
print ("A diferença absoluta de dois numeros é :",diferenca)
