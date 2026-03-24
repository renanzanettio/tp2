from tkinter import *

class Aplicacao:
    def __init__(self):
        self.tela = Tk()
        self.configurar_tela()
        self.criar_componente()

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
        self.txtnome = Entry(self.tela, width=20, borderwidth= 3)
        self.txtnome.pack()

    def executar(self):
        self.tela.mainloop()
        