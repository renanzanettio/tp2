numero = int(input("Digite um número: "))

if numero % 2 == 0:
    resultado = numero ** 2
    print(f"O número {numero} é par e seu quadrado é {resultado}")
else:
    resultado = numero ** 3
    print(f"O número {numero} é ímpar e seu cubo é {resultado}")