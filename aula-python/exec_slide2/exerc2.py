nome1 = input("Digite o nome da primeira pessoa: ")
pes1 = float(input("Digite o peso da primeira pessoa: "))
nome2 = input("Digite o nome da segunda pessoa: ")
pes2 = float(input("Digite o peso da segunda pessoa: "))

if pes1 == pes2:
    print(f"{nome1} e {nome2} tem o mesmo peso")
elif pes1 > pes2:
    print(f"{nome1} tem o maior peso, com {pes1}kg")
else:
    print(f"{nome2} tem o maior peso, com {pes2}kg")