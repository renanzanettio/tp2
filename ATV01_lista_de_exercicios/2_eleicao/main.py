brancos = int(input("Votos brancos: "))
nulos = int(input("Votos nulos: "))
validos = int(input("Votos válidos: "))

total = brancos + nulos + validos

perc_brancos = (brancos * 100) / total
perc_nulos = (nulos * 100) / total
perc_validos = (validos * 100) / total

print(f"Total de eleitores: {total}")
print(f"Brancos: {perc_brancos}%")
print(f"Nulos: {perc_nulos}%")
print(f"Válidos: {perc_validos}%")