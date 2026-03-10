class Produto:
    def __init__(self):
        self.nome = ""
        self.__valor = 0.0
        self.__qtd = 0

    # ENCAPSULAMENTO
    #getter nome
    def get_Nome(self):
        return self.__nome
    #setter nome
    def set_Nome(self, nome):
        self.__nome = nome

    #getter qtd
    def get_Qtd(self):
        return self.__qtd
    #setter qtd
    def set_Qtd(self, qtd):
        self.__qtd = qtd
        
    #getter valor
    def get_Valor(self):
        return self.__valor
    #setter valor
    def set_Valor(self, valor):
        self.__valor = valor

    #metodo cadastrar
    def cadastrarProduto(self):
        print("\n === Cadastro de Produtos === \n")
        self.set_Nome(input("Nome do Produto: "))
        self.set_Qtd(int(input("Quantidade do Produto: ")))
        self.set_Valor(float(input("Valor do Produto: ")))

    #método mostrar
    def mostrarProduto(self):
        print("\n === Dados do Produto === \n")
        print("Nome do Produto: ", self.get_Nome())
        print("Quantidade do Produto: ", self.get_Qtd())
        print("Valor do Produto: ", self.get_Valor())

    #método calcular
    def calcular(self):
        return self.__qtd * self.__valor