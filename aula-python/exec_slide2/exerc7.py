rg = input("Digite o RF: ")
anonascimento = int(input("Digite o ano de nascimento: "))
anoingresso = int(input("Digite o ano de ingresso na empresa: "))
anoatual = int(input("Digite o ano atual: "))

idade = anoatual - anonascimento
tempo = anoatual - anoingresso

print(f"\nIdade: {idade}")
print(f"Tempo de trabalho: {tempo}")

if idade >= 65 or tempo >= 30 or (idade >= 60 and tempo >= 25):
    print("Requerer aposentadoria")
else:
    print("Não requerer aposentadoria")