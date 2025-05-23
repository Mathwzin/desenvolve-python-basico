#Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu tempo de serviço (em anos) e escreva uma expressão que imprima True se a pessoa já pode se aposentar, ou False caso contrário, de acordo com as seguintes regras:
#A: Para mulheres, ter mais de 60 anos. Para homens, 65.
#B: Ou ter trabalhado pelo menos 30 anos.
#C: Ou ter 60 anos  e trabalhado pelo menos 25.

genero =  str (input("Qual seu genero (m) ou (f):"))
idade = int (input("Qual sua idade : "))
tempo_servico =  int (input("Quanto tempo de serviço"))
a= (genero =='m' and idade >= 65) or (genero == 'f' and idade >=60)
b= tempo_servico >=30
c= idade >= 60  and tempo_servico >= 25
verificador = a or b or c 
print ("Pode se aposentar :", verificador)