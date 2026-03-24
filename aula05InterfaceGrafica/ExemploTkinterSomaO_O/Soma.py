from tkinter import *

class Soma_Numeros:
    def __init__(self):
        self.tela = Tk()
        self.configurar_tela()
        self.criar_componente()
        self.calcular()

    def configurar_tela(self):
        self.tela.title("Aplicação O_O")
        self.tela.configure(background="#1e3743")

        largura = 800
        altura = 300

        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()

        #DEFINE O POSICIONAMENTO CENTRALIZADO
        posx = largura_screen / 2 - largura /2
        posy = altura_screen / 2 - altura /2

        #CONSTROI A TELA DE ACORDO COM AS DIMENSÕES DA TELA DE WINDOWS
        self.tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

    def criar_componente(self):
        self.frame = Frame(self.tela, bg="#34495a", padx = 20, pady = 20)
        self.frame.pack(expand=True)

        self.titulo = Label(self.frame , text="Soma de Numeros")
        #grid => cria grade row = linha; column = coluna; colmspam = espaço interno coluna
        self.titulo.grid(row=0, column=0, columnspan=2, pady=10)

        Label(self.frame, text="Numero 1:").grid(row=1 , column=0, sticky= "w", pady=5)

        self.txt_n1 = Entry(self.frame)
        self.txt_n1.grid(row=1, column=1, pady=5)

        Label(self.frame, text="Numero 2:").grid(row=3, column=0, sticky="w", pady=5)

        self.txt_n2 = Entry(self.frame)
        self.txt_n2.grid(row=3, column=1, pady=5)

        self.txt_resu1 = Entry(self.frame)
        self.txt_resu1.grid(row=4, column=1, pady=5)

        self.btn_botao = Button(self.frame, text= "Calcular", command= self.calcular)
        self.btn_botao.grid(row = 5, column=0, columnspan=2, pady=15)

    def calcular(self):
        self.__n1 = float(self.txt_n1.get())
        self.__n2 = float(self.txt_n2.get())
        self.__soma = self.__n1 + self.__n2

        self.txt_resu1.insert(0, self.__soma)

    def executar(self):
        self.tela.mainloop()
        
    