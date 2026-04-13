class Loja:
    def __init__(self):
        self.__razaoSocial = ""
        self.__cpfCliente = ""
        self.__valorCompra = 0.0
        self.__qtdItensComp = 0
        self.__valorTotalCompra = 0.0

    def inserirDadosLoja(self):
        self.__razaoSocial = input("Razão Social: ")
        self.__cpfCliente = input("CPF do Cliente: ")
        self.__valorCompra = float(input("Valor da compra: "))
        self.__qtdItensComp = int(input("Quantidade de itens: "))

    def calcularCompraLoja(self):
        self.__valorTotalCompra = self.__valorCompra * self.__qtdItensComp
        return self.__valorTotalCompra

    def mostrarDadosLoja(self):
        return f"Razão Social: {self.__razaoSocial}\nCPF: {self.__cpfCliente}\nTotal: R$ {self.__valorTotalCompra}"