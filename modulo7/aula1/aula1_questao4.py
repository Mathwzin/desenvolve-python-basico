# 4.Faça um programa que leia um número de celular e, caso o número tenha apenas 8 dígitos, acrescente o 9 na frente.
# Caso o número já tenha 9 dígitos, verifique se o primeiro dígito é 9. Adicione o separador "-" na sua impressão.
telefone  = input("Digite o número: ")
if len(telefone) == 8:
    numero_completo =  '9' + telefone
    print("Número completo: ",numero_completo)
elif len(telefone) == 9:
    numero_completo = telefone[:5] + '-' + telefone[5:]
    print("Número completo: ",numero_completo)