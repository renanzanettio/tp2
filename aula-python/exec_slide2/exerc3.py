altura = float(input("Digite a altura: "))
sexo = input("Digite o sexo (M/F): ")

if sexo.upper() == "M":
    peso = (72.7 * altura) - 58
else:
    peso = (62.1 * altura) - 44.7

print(f"Altura: {altura}")
print(f"Sexo: {sexo.upper()}")
print(f"Peso ideal: {peso:.2f}")