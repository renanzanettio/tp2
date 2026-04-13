from Loja import Loja

class Main:
    def main():
        loja = Loja()
        loja.inserirDadosLoja()
        loja.calcularCompraLoja()
        print(loja.mostrarDadosLoja())    

if __name__ == "__main__":
    Main.main()