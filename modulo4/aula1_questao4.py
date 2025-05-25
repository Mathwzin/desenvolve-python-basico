# Transforme em código o fluxograma a seguir

n = int (input("Digite o valor de n: "))
maior = 0
while n > 0:
    x = int(input("Digite o  número X: "))
    if x > maior:
        maior = x
    n = n - 1
print("O maior número é:", maior)