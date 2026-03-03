import os 
os.system("cls")


#Estrutura IF Operadores Relacionais "and = e" e "or = ou"

n1 = int(input("Digite o primeiro numero:"))
n2 = int(input("Digite o segundo numero:"))
n3 = int(input("Digite o terceiro numero:"))

if n1 == n2 or n2 == n3 or n1 == n3:
    exit() #termina a execução
if n1 > n2 and n1 > n3:
    print("O primeiro número é o maior.")
if n2 > n1 and n2 > n3:
    print("O segundo número é o maior.")
if n3 > n1 and n3 > n2:
    print("O terceiro número é o maior.")

