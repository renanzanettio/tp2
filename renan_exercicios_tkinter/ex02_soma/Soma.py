from tkinter import *

class Soma:
    def __init__(self):
        self.tela = Tk()
        self.configurar_tela()
        self.criar_componentes()

        # Atributos Privados
        self.__num1 = 0
        self.__num2 = 0
        self.__soma = 0

    @property
    def _num1(self):
        return self.__num1

    @_num1.setter
    def _num1(self, value):
        self.__num1 = value

    @property
    def _num2(self):
        return self.__num2

    @_num2.setter
    def _num2(self, value):
        self.__num2 = value

    @property
    def _soma(self):
        return self.__soma

    @_soma.setter
    def _soma(self, value):
        self.__soma = value

    def configurar_tela(self):
        self.tela.title("Calculo Soma")
        self.tela.configure(background="#f1f1f1")

        largura = 420
        altura = 320

        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()

        posx = largura_screen / 2 - largura / 2
        posy = altura_screen / 2 - altura / 2

        self.tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

    def criar_componentes(self):
        self.frame = Frame(self.tela, bg="#333", padx=20, pady=20)
        self.frame.pack(expand=True)

        self.titulo = Label(self.frame, text="CALCULO SOMA", bg="#333", fg="white", font=("Arial", 14, "bold"))
        self.titulo.grid(row=0, column=0, columnspan=2, pady=10)

        Label(self.frame, text="Digite um número:", bg="#333", fg="white", font="Arial").grid(row=1, column=0, sticky="w", pady=5)
        self.txt_n1 = Entry(self.frame, width=20, bg="#ecf0f1")
        self.txt_n1.grid(row=1, column=1, pady=5)

        Label(self.frame, text="Digite um segundo número:", bg="#333", fg="white", font="Arial").grid(row=2, column=0, sticky="w", pady=5)
        self.txt_n2 = Entry(self.frame, width=20, bg="#ecf0f1")
        self.txt_n2.grid(row=2, column=1, pady=5)

        Label(self.frame, text="Resultado:", bg="#333", fg="white", font="Arial").grid(row=3, column=0, sticky="w", pady=5)
        self.txt_resul = Entry(self.frame, width=20, bg="#ecf0f1")
        self.txt_resul.grid(row=3, column=1, pady=5)

        self.lbl_resultado = Label(self.frame, text="", bg="white", font=("Arial", 10), width=30, pady=6)
        self.lbl_resultado.grid(row=4, column=0, columnspan=2, pady=5)

        self.btn_calcular = Button(self.frame, text="Calcular Soma", font=("Arial", 10, "bold"), command=self.calcular)
        self.btn_calcular.grid(row=5, column=0, columnspan=2, pady=15)

    def calcular(self):
        self.__num1 = float(self.txt_n1.get())
        self.__num2 = float(self.txt_n2.get())
        self.__soma = self.__num1 + self.__num2

        self.txt_resul.delete(0, END)
        self.txt_resul.insert(0, self.__soma)

        self.lbl_resultado.config(text=f"Resultado: {self.__soma}")

    def executar(self):
        self.tela.mainloop()
