tabuada = int(input("Tabuada de: "))
i = int(input("De: "))
fim = int(input("Até: "))

while i <= fim:
    resultado = tabuada * i
    print(f"{tabuada} x {i} = {resultado}")
    i += 1