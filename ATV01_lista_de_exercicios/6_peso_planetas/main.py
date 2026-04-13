peso_terra = float(input("Digite o peso na Terra (kg): "))

print("1. Mercúrio")
print("2. Vênus")
print("3. Marte")
print("4. Júpiter")
print("5. Saturno")
opcao = int(input("Escolha o número de um planeta: "))

match opcao:
    case 1:
        peso_final = peso_terra * 0.37
        print(f"Peso em Mercúrio: {peso_final}")
    case 2:
        peso_final = peso_terra * 0.88
        print(f"Peso em Vênus: {peso_final}")
    case 3:
        peso_final = peso_terra * 0.38
        print(f"Peso em Marte: {peso_final}")
    case 4:
        peso_final = peso_terra * 2.64
        print(f"Peso em Júpiter: {peso_final}")
    case 5:
        peso_final = peso_terra * 1.15
        print(f"Peso em Saturno: {peso_final}")
    case _:
        print("Opção inválida")