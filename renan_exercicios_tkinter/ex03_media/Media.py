from tkinter import *

class Media:
    def __init__(self):
        self.tela = Tk()
        self.configurar_tela()
        self.criar_componentes()

        # Atributos Privados
        self.__n1 = 0.0
        self.__n2 = 0.0
        self.__n3 = 0.0
        self.__media = 0.0

    @property
    def _n1(self):
        return self.__n1

    @_n1.setter
    def _n1(self, value):
        self.__n1 = value

    @property
    def _n2(self):
        return self.__n2

    @_n2.setter
    def _n2(self, value):
        self.__n2 = value

    @property
    def _n3(self):
        return self.__n3

    @_n3.setter
    def _n3(self, value):
        self.__n3 = value

    @property
    def _media(self):
        return self.__media

    @_media.setter
    def _media(self, value):
        self.__media = value

    def configurar_tela(self):
        self.tela.title("Calculo Média")
        self.tela.configure(background="#f1f1f1")

        largura = 420
        altura = 380

        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()

        posx = largura_screen / 2 - largura / 2
        posy = altura_screen / 2 - altura / 2

        self.tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

    def criar_componentes(self):
        self.frame = Frame(self.tela, bg="#333", padx=20, pady=20)
        self.frame.pack(expand=True)

        self.titulo = Label(self.frame, text="CALCULO MÉDIA", bg="#333", fg="white", font=("Arial", 14, "bold"))
        self.titulo.grid(row=0, column=0, columnspan=2, pady=10)

        Label(self.frame, text="Digite a primeira nota:", bg="#333", fg="white", font="Arial").grid(row=1, column=0, sticky="w", pady=5)
        self.txt_n1 = Entry(self.frame, width=20, bg="#ecf0f1")
        self.txt_n1.grid(row=1, column=1, pady=5)

        Label(self.frame, text="Digite a segunda nota:", bg="#333", fg="white", font="Arial").grid(row=2, column=0, sticky="w", pady=5)
        self.txt_n2 = Entry(self.frame, width=20, bg="#ecf0f1")
        self.txt_n2.grid(row=2, column=1, pady=5)

        Label(self.frame, text="Digite a terceira nota:", bg="#333", fg="white", font="Arial").grid(row=3, column=0, sticky="w", pady=5)
        self.txt_n3 = Entry(self.frame, width=20, bg="#ecf0f1")
        self.txt_n3.grid(row=3, column=1, pady=5)

        Label(self.frame, text="Resultado:", bg="#333", fg="white", font="Arial").grid(row=4, column=0, sticky="w", pady=5)
        self.txt_resul = Entry(self.frame, width=20, bg="#ecf0f1")
        self.txt_resul.grid(row=4, column=1, pady=5)

        self.lbl_resultado = Label(self.frame, text="", bg="white", font=("Arial", 10), width=30, pady=6)
        self.lbl_resultado.grid(row=5, column=0, columnspan=2, pady=5)

        self.btn_calcular = Button(self.frame, text="Calcular Média", font=("Arial", 10, "bold"), command=self.calcular)
        self.btn_calcular.grid(row=6, column=0, columnspan=2, pady=15)

    def calcular(self):
        self.__n1 = float(self.txt_n1.get())
        self.__n2 = float(self.txt_n2.get())
        self.__n3 = float(self.txt_n3.get())
        self.__media = (self.__n1 + self.__n2 + self.__n3) / 3

        media_fmt = round(self.__media, 2)

        self.txt_resul.delete(0, END)
        self.txt_resul.insert(0, media_fmt)

        if self.__media >= 7:
            situacao = "Aprovado"
        elif self.__media >= 3:
            situacao = "Exame"
        else:
            situacao = "Reprovado"

        self.lbl_resultado.config(text=f"Resultado Média: {media_fmt}\nAluno {situacao}")

    def executar(self):
        self.tela.mainloop()
