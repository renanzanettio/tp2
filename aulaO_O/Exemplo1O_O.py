# Criar CLasse Carro

class Carro:
    #construtor da classe
    def __init__(self, nome):
        self.nome = nome;

    #método da classe carro
    def acelerar(self):
        print(self.nome, " está acelerando...")

#instanciando objeto car da classe Carro
car = Carro("Fusca")
print(car.nome)
car.acelerar()


car = Carro("Uno")
print(car.nome)
car.acelerar()
