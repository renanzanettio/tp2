class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    #método calcular idade
    def calcularIdade(self):
        anoatual = int(input("Digite o ano atual: "))
        return anoatual - self.idade

#instanciar objeto da classe pessoa
p1 = Pessoa('Luiz', 25)
p2 = Pessoa('Joao', 56)
print(p1.calcularIdade())
print(self.nome, " voce nasceu em ", p2.calcularIdade())
