num = float(input("Digite o numero: "))
exp = float(input("Digite o expoente: "))

#Potencia usando operador
potOperador = num ** exp
#Potencia math
potFuncao = pow(num, exp)

print(f"O resultado da potencia é {potFuncao} ou {potOperador}")