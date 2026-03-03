#exemplo for utilizando lista de valores pré-definida

frutas = ['banana', 'abacaxi', 'goiaba', 'abacate']
for lista in frutas:
    print(lista)


buscar = 'goiaba'
frutas = ['banana', 'abacaxi', 'goiaba', 'abacate']
for i in frutas:
    if i == buscar:
        print(f"Fruta encontrada {buscar}")
        break
    else:
        print(f"Fruta nao encontradac{buscar}")