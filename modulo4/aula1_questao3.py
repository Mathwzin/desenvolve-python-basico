#Transforme em código o fluxograma a seguir

n1 = int (input("Digite o valor de n1: "))
n2 = int (input("Digite o valor de n2: "))
n3 = int (input("Digite o valor de n3: "))
m =  (n1+ n2 + n3)/3 
print (m)
if(m>=60):
    print("Aprovado!")
elif(m>=40):
    print("Recuperação!")
else:
    print("Reprovado!")
print ("Fim!")