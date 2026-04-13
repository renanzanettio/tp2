from Matematica import Matematica

class Main:
    def main():
        prova = Matematica()
        prova.inserirNotas()
        prova.calcularMedia()
        print(prova.mostrarNomeMedia())

if __name__ == "__main__":
    Main.main()