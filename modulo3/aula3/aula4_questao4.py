#Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do pacote. 
#Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. 
# O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:
#Distância até 100 km: R$1 por kg.
#Distância entre 101 e 300 km: R$1.50 por kg.
#Distância acima de 300 km: R$2 por kg.
#Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg

km = float(input("Digite distância da entrega em quilômetros: "))
kg = float(input("Digite o peso entrega em quilogramas: "))
if kg > 10 :   
    if km <= 100:
        valor = kg * 1 + 10 
        print("O Frete é de R$:", valor)
    if (km <= 300) and (km >=101):
        valor = kg * 1.5 + 10 
        print("O Frete é de R$:", valor)
    if km > 300:
        valor = kg * 2 + 10 
        print("O Frete é de R$:", valor)
else:
    if km <= 100:
        valor = kg * 1 
        print("O Frete é de R$:", valor)
    if (km <= 300) and (km >=101):
        valor = kg * 1.5 
        print("O Frete é de R$:", valor)
    if km > 300:
        valor = kg * 2 
        print("O Frete é de R$:", valor)

