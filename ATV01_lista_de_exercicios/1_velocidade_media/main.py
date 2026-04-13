brancos = int(input("Digite a quantidade de votos brancos: "))
nulos = int(input("Digite a quantidade de votos nulos: "))
validos = int(input("Digite a quantidade de votos válidos: "))

total = brancos + nulos + validos

perc_brancos = (brancos * 100) / total
perc_nulos = (nulos * 100) / total
perc_validos = (validos * 100) / total

print(f"Total de eleitores: {total}")
print(f"Brancos: {perc_brancos}%")
print(f"Nulos: {perc_nulos}%")
print(f"Válidos: {perc_validos}%")