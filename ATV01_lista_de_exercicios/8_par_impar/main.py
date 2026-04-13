pares = []
impares = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}° número: "))
    
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")