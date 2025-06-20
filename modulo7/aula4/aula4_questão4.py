# Vamos fazer o jogo da forca! Antes de programar: 
#Crie um arquivo no seu computador chamado "gabarito_forca.txt" com uma lista de 10 palavras de sua escolha (separadas por quebras de linha, "\n"). 
#Essas serão as opções de palavra do jogo.
#Crie um arquivo chamado "gabarito_enforcado.txt" com o conteúdo apresentado ao final dessa questão.
#Escreva um programa em Python para executar o jogo, de acordo com as definições:
#Abra o arquivo "gabarito_forca.txt" e escolha aleatoriamente uma palavra;
#Com o arquivo "gabarito_enforcado.txt", crie uma lista de strings com os estágios do enforcado;
#No início exiba o número de letras na palavra como underscores;
#Permita que o jogador insira letras para adivinhar a palavra;
#Em caso de acerto, mostre o progresso do jogador substituindo os underscores correspondentes à letra digitada;
#Em caso de erro, crie a função "imprime_enforcado()" que recebe um inteiro indicando o número de erros do jogador e imprime o enforcado correspondente;
# Limite o número de tentativas para 6 (as partes do enforcado).
import os, random 
with open('gabarito.txt','w')as f:
    f.write("programacao\n")
    f.write("computador\n")
    f.write("pudim\n")
    f.write("trap\n")
    f.write("linux\n")
    f.write("lodo\n")
    f.write("sorvete\n")
    f.write("musica\n")
    f.write("luz\n")
    f.write("corrente\n")
with open('gabarito.txt', 'r', encoding='utf-8') as f:
    palavras = f.read().splitlines()
palavra = random.choice(palavras)
letras_descobertas = ['_' for _ in palavra]
tentativas = 6
erros = 0
letras_usadas = []
with open('gabarito_enforcado.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()
estagios = conteudo.strip().split('\n\n')

def imprime_enforcado(erro):
    print(estagios[erro])

print("🎮 Bem-vindo ao Jogo da Forca!")

while erros < tentativas and '_' in letras_descobertas:
    print("\nPalavra:", ' '.join(letras_descobertas))
    print(f"Letras usadas: {', '.join(letras_usadas)}")
    letra = input("Digite uma letra: ").lower()

    if not letra.isalpha() or len(letra) != 1:
        print("Por favor, digite apenas **uma letra**.")
        continue

    if letra in letras_usadas:
        print("Você já usou essa letra. Tente outra.")
        continue

    letras_usadas.append(letra)

    if letra in palavra:
        for i, l in enumerate(palavra):
            if l == letra:
                letras_descobertas[i] = letra
        print("✅ Acertou!")
    else:
        erros += 1
        print("❌ Errou!")
        imprime_enforcado(erros)

if '_' not in letras_descobertas:
    print("\n Parabéns! Você venceu!")
else:
    imprime_enforcado(erros)
    print("\nGAME OVER. Você foi enforcado.")

print("A palavra era:", palavra)