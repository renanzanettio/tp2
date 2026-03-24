from Aplicacao import Aplicacao

class Principal:
    @staticmethod
    def main():
        #instanciar classe aplicacao
        apl = Aplicacao()
        apl.executar()

if __name__ == "__main__":
    Principal.main()