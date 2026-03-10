class Produto:
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    def mostrar(self):
        print("Nome Produto: ", self.nome)
        print("Preço Produto: R$ ", self.preco)
        print("Quantidade: ", self.qtd)

    def calcularTotal(self):
        valor_total = self.qtd * self.preco
        print(f"O valor total é R${valor_total}")

prod = Produto("abacate", 4.9, 76)
prod.mostrar()
prod.calcularTotal()