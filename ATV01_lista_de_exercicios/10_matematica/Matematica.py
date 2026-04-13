class Matematica:
    def __init__(self):
        self.__nota1 = 0.0
        self.__nota2 = 0.0
        self.__media = 0.0
        self.__nomeAluno = ""

    def inserirNotas(self):
        self.__nomeAluno = input("Nome do aluno: ")
        self.__nota1 = float(input("Digite a nota 1: "))
        self.__nota2 = float(input("Digite a nota 2: "))

    def calcularMedia(self):
        self.__media = (self.__nota1 + self.__nota2) / 2
        return self.__media

    def mostrarNomeMedia(self):
        return f"A média do aluno {self.__nomeAluno} é {self.__media}"