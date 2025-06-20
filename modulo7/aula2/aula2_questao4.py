# Implemente uma função em Python chamada validador_senha() que verifica se uma senha fornecida atende todos os seguintes critérios:
# Pelo menos 8 caracteres de comprimento.
# Contém pelo menos uma letra maiúscula e uma letra minúscula.
# Contém pelo menos um número.
# Contém pelo menos um caractere especial (por exemplo, @, #, $).
import string   
def validador_senha(senha):
    if len(senha) < 8:
        return False
    tem_maiuscula = False
    tem_minuscula = False
    tem_digito = False
    tem_especial = False
    for c in senha:
        if c.isupper():
            tem_maiuscula = True
        elif c.islower():
            tem_minuscula = True
        elif c.isdigit():
            tem_digito = True
        elif c in string.punctuation:
            tem_especial = True

    return tem_maiuscula and tem_minuscula and tem_digito and tem_especial
  
senha = input ("Digite uma senha: ")
print(validador_senha(senha))