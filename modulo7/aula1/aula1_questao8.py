def calcular_digito(cpf_parcial, peso_inicial):
    soma = 0
    for i in range(len(cpf_parcial)):
        soma += int(cpf_parcial[i]) * (peso_inicial - i)
    resto = soma % 11
    if resto < 2:
        return '0'
    else:
        return str(11 - resto)
def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    if len(cpf) != 11 or not cpf.isdigit():
        return "Inválido"
    nove_digitos = cpf[:9]
    digito1 = calcular_digito(nove_digitos, 10)
    dez_digitos = nove_digitos + digito1
    digito2 = calcular_digito(dez_digitos, 11)
    if cpf[-2:] == digito1 + digito2:
        return "Válido"
    else:
        return "Inválido"
cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")
resultado = validar_cpf(cpf)
print("CPF:", resultado)
