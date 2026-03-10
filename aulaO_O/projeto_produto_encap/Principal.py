# IMPORTAR A CLASSE PRODUTO
from Produto import Produto
class Principal:
    @staticmethod
    def main():
        #instanciar classe Produto()
        prod = Produto()
        #chamar os métodos
        prod.cadastrarProduto()
        prod.mostrarProduto()
        print(f"Valor total = {prod.calcular()}")

#define a inciialização pela classe Principal
if __name__ == "main":
    Principal.main()