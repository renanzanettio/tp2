from Funcionario import Funcionario

class Principal:
    def main():
        func = Funcionario()

        func.cadastrarFunc()
        print(f"O aumento é R${func.calcularAumento()}")

if __name__ == "__main__":
    Principal.main()