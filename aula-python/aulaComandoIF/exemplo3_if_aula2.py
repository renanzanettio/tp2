import os 
os.system("cls")

print("$$$ Programa de Empréstimos $$$ /n Responda (0-NÃO 1-SIM)")

neg = int(input("Possui nome negativo? "))
if neg == 1:
    print("Você não pode fazer um empréstimo")
else:
    cartass = int(input("Você possui carteira assinada? "))
    if cartass == 0:
        print("Você não pode fazer um empréstimo")
    else:
        casa = int(input("Pessui casa prória? "))
        if casa == 0:
            print("Você não pode realizar empréstimo")
        else:
            print("Conceder o empréstimo[]")