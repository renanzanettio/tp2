n1 = int(input("Digite o primeiro numero"))
n2 = int(input("Digite o segundo numero"))

if n1 == n2:
    print("O primeiro numero é o mesmo do segundo, a divisao deles resulta em 1")
elif n1 > n2:
    divisao = n1/n2
else:
    divisao = n2/n1

print(f"O resultado da divisao é {divisao}")