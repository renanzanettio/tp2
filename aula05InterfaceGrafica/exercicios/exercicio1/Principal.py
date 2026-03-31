from Clientes import cadastrarCliente

class Principal:
    @staticmethod
    def main():
        # Instanciar Classe Aplicacao
        dados = cadastrarCliente()
        dados.executar()

if __name__ == "__main__":
    Principal.main()