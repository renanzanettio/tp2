num1 = float(input("Digite o primeiro número positivo: "))
num2 = float(input("Digite o segundo número positivo: "))

print("1. Média ponderada")
print("2. Quadrado da soma")
print("3. Cubo do menor número")
opcao = int(input("Digite o numero para escolher uma opção: "))

match opcao:
    case 1:
        media = (num1 * 2 + num2 * 3) / 5
        print(f"Média ponderada: {media}")
    case 2:
        soma_quadrado = (num1 + num2) ** 2
        print(f"Quadrado da soma: {soma_quadrado}")
    case 3:
        if num1 < num2:
            menor = num1
        else:
            menor = num2
        cubo = menor ** 3
        print(f"Cubo do menor ({menor}): {cubo}")
    case _:
        print("Opção inválida")