#Dada uma lista de endereços web (URLs) que sempre começam com "www." e sempre terminam com ".com", 
#use o conceito de fatiamento de listas para criar uma lista dominios com o nome principal de todos os domínios, conforme exemplo a seguir. 
URLs = []
dominios = []
while True:
    url = (input("Digite as urls (Para finalizar digite FIM): "))
    if url == 'FIM':
        break
    if url != 'FIM':
        URLs.append(url)
for url in URLs:
    dominio = url[4:-4] 
    dominios.append(dominio) 
print(URLs)
print(dominios)