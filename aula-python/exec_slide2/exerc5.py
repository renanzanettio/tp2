alt1 = float(input("Digite a altura da primeira pessoa: "))
alt2 = float(input("Digite a altura da segunda pessoa: "))
alt3 = float(input("Digite a altura da terceira pessoa: "))

alturas = [alt1, alt2, alt3]

alturas.sort()

print(f"Maior altura: {alturas[2]}")
print(f"Altura mediana: {alturas[1]}")
print(f"Menor altura: {alturas[0]}")