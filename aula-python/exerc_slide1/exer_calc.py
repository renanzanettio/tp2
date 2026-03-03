n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))

operacao = input("escolha a operação: \n 1 - adicao \n 2- subtracao  \n 3 - multiplicacao \n 4 - divisao \n")

def adicao(n1, n2):
    return n1 + n2
def subtracao(n1, n2):
    return n1 - n2
def multiplicacao(n1, n2):
    return n1 * n2
def divisao(n1, n2):
    return n1 / n2

if operacao == '1':
    resultado = adicao(n1, n2)
elif operacao == '2':
    resultado = subtracao(n1, n2)
elif operacao == '3':
    resultado = multiplicacao(n1, n2)
elif operacao == '4':
    resultado = divisao(n1, n2)
else:
    resultado = "Operação invalida"


print(f"O resultado é {resultado}")

