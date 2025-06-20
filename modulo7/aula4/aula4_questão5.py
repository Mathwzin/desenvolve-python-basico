#A extensão ".csv" significa "comma-separated values" ou "valores separados por vírgula". É a extensão utilizada por sistemas de gerência de tabelas como o Microsoft Excel ou Google Sheets. Nesse exercício vamos criar uma planilha com dados sobre livros que você já leu ou gostaria de ler. Siga as instruções.
#Selecione pelo menos 10 livros que você leu ou gostaria de ler. Você deve reunir as seguintes informações: título, autor, ano de publicação e número de páginas.
#No Python, crie um arquivo chamado "meus_livros.csv", aberto para escrita.
#Na primeira linha escreva os títulos da planilha separados por vírgula (sem espaço em branco). Os títulos são: "Título", "Autor", "Ano de publicação" e "Número de páginas". Lembre de finalizar a linha com uma quebra de linha.
# A partir da segunda linha escreva as informações de cada livro que você levantou, separando cada informação por uma vírgula (sem espaço em branco). Lembre de finalizar cada linha com uma quebra de linha.
#Feche o arquivo para salvá-lo e abra com a ferramenta de planilhas de sua escolha. Como você já tem conta no Google, sugiro abrir com o Google Sheets.
import os, csv
livro = [
    ["Duna", "Frank Herbert", 1965, 688],
    ["Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 223],
    ["O Senhor dos Anéis: A Sociedade do Anel",	"J.R.R. Tolkien", 1954, 423],
    ["Percy Jackson e o Ladrão de Raios", "Rick Riordan",	2005, 377],
    ["As Crônicas de Nárnia: O Leão, a Feiticeira e o Guarda-Roupa", "C.S. Lewis", 1950, 208],
    ["A Dança dos Dragões", "George R.R Martin", 2011, 832],
    ["A Guerra dos Tronos : As Crônicas de Gelo e Fogo", "George R.R Martin", 1996, 592],
    ["O Hobbit", "J.R.R. Tolkien", 1937, 320],
    ["O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96],
    ["1984", "George Orwell", 1949, 328]
]
with open('meus_livros.csv', 'w', newline='',) as f:
    escritor = csv.writer(f)
    escritor.writerow(["Título", "Autor", "Ano de publicação", "Número de páginas"])
    escritor.writerows(livro)