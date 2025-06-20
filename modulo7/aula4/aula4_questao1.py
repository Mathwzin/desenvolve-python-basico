#Escreva um script Python que solicita uma frase do usuário e a salve em um arquivo chamado "frase.txt" no mesmo local do seu script.
#Imprima em seguida o caminho completo do arquivo salvo.
import os
frase = input("Digite uma frase: ")
os.listdir()
f =  open('arquivo.txt','w', encoding='utf-8')
type(f)
f.write(frase)
f.close()
