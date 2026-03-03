num = int(input("Digite um número inteiro positivo: "))

if num % 2 == 0:
    result = num ** 2
    print("O número é par")
else:
    result = num ** 3
    print("O número é ímpar")

print(f"o resultado é {result}")