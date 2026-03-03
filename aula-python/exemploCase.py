opc = int(input(" 1 - Sacar \n 2 - Extrato \n 3 - Sair \n Escolha a opção:"))

match opc:
    case 1:
        print("voce escolheu a opção sacar")
        valor = float(input("Digite o valor do saque"))
        print(f"sacando da sua conta .... o valor de R$ {valor}")
    case 2:
        print("voce escolheu a opção Extrato")
        dias = int(input("Digite a quantidade de dias: "))
        print(f"Retirando o extrato de {dias} dias . . .")
    case 3:
        print("Saindo do programa")
    case _:
        print("Opção invalida")