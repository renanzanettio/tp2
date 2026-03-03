
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

#comando if
if media > 6.0:
    print(f"Aprovado. A média do aluno é {media:.2f}")
elif media > 5.0 and media < 6.0:
    print(f"O aluno está de exame. A média dele é {media:.2f}")
else:
    print(f"Reprovado. A média do aluno é {media:.2f}")

