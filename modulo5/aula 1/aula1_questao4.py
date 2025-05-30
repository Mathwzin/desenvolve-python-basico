#Escreva um programa em Python que utiliza a biblioteca datetime para exibir a data e hora atuais com a formatação apresentada a seguir:
from datetime import datetime 
agora = datetime.now()
data_formatada = agora.strftime("%d/%m/%Y")
hora_formatada = agora.strftime ("%H:%M:%S")
print("Data atual:",data_formatada)
print("Hora atual:",hora_formatada)