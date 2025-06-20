#Crie a função encrypt() que recebe uma lista de strings e retorna os nomes criptografados, bem como a chave da criptografia. Regras:
# Chave de criptografia: gere um valor n aleatório entre 1 e 10
# Substitua cada caracter c pelo caracter c + n. Trabalharemos apenas com o intervalo de caracteres visíveis (entre 33 e 126 na tabela Unicode)
import random 
def encrypt(lista_nome):
    chave = random.randint(1, 10)
    nomes_criptografados = []

    for n in lista_nome:
        nome_criptografado = "" 
        for c in n:
            codigo = ord(c) + chave
            if codigo > 126:
                codigo = 33 + (codigo - 127)
            nome_criptografado += chr(codigo)
        nomes_criptografados.append(nome_criptografado)
    
    return nomes_criptografados, chave

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
criptografados, chave = encrypt(nomes)
print("Chave aleatória:", chave)
print("Nomes criptografados:", criptografados)