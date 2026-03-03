num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

print("\menu")
print("1 - media ponderada")
print("2 - quadrado da soma")
print("3 - cubo do menor numero")

opcao = int(input("escolha uma opção: "))

if opcao == 1:
    media = (num1 * 2 + num2 * 3) / 5
    print(f"media ponderada: {media}")

elif opcao == 2:
    resultado = (num1 + num2) ** 2
    print(f"quadrado da soma {resultado}")

elif opcao == 3:
    if num1 > num2:
        menor = num2
    if num2 > num1:
        menor = num1
    
    cubo = menor ** 3
    print(f"cubo do menor numero ({menor}): {cubo}")

else:
    print("opcao nao existe")