#Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.
# Dica: usando listas você não precisa fazer um "if" para cada mê.
data_nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")
mes = data_nascimento [3:5]
dia = data_nascimento[:2]
ano= data_nascimento [-4:]
if mes == "01":
    print(f"Você nasceu em {dia} de Janeiro de {ano}.")
elif mes == "02":
    print(f"Você nasceu em {dia} de Fevereiro de {ano}.")
elif mes == "03":
    print(f"Você nasceu em {dia} de Março de {ano}.")
elif mes == "04":
    print(f"Você nasceu em {dia} de Abril de {ano}.")
elif mes == "05":
    print(f"Você nasceu em {dia} de Maio de {ano}.")
elif mes == "06":
    print(f"Você nasceu em {dia} de Junho de {ano}.")
elif mes == "07":
    print(f"Você nasceu em {dia} de Julho de {ano}.")
elif mes == "08":
    print(f"Você nasceu em {dia} de Agosto de {ano}.")
elif mes == "09":
    print(f"Você nasceu em {dia} de Setembro de {ano}.")    
elif mes == "10":
    print(f"Você nasceu em {dia} de Outubro de {ano}.")
elif mes == "11":
    print(f"Você nasceu em {dia} de Novembro de {ano}.")
elif mes == "12":
    print(f"Você nasceu em {dia} de Dezembro de {ano}.")
else:
    print("Inválido!")
