print("**** CÁLCULO DE GRANDEZAS ELÉTRICAS ****")
print("1. Tensão")
print("2. Resistência")
print("3. Corrente")
opcao = int(input("Digite um número para escolher uma opção: "))

match opcao:
    case 1:
        resistencia = float(input("Digite a resistência (R): "))
        corrente = float(input("Digite a corrente (i): "))
        tensao = resistencia * corrente
        print(f"Tensão: {tensao} V")
    case 2:
        tensao = float(input("Digite a tensão (U): "))
        corrente = float(input("Digite a corrente (i): "))
        resistencia = tensao / corrente
        print(f"Resistência: {resistencia} R")
    case 3:
        tensao = float(input("Digite a tensão (U): "))
        resistencia = float(input("Digite a resistência (R): "))
        corrente = tensao / resistencia
        print(f"Corrente: {corrente} A")
    case _:
        print("Opção inválida")