from tkinter import *

class Produto:
    def __init__(self):
        self.tela = Tk()
        self.configurar_tela()
        self.criar_componentes()

        # Atributos Privados
        self.__nome = ""
        self.__quantidade = 0
        self.__valor = 0.0
        self.__total = 0.0

    @property
    def _nome(self):
        return self.__nome

    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _quantidade(self):
        return self.__quantidade

    @_quantidade.setter
    def _quantidade(self, value):
        self.__quantidade = value

    @property
    def _valor(self):
        return self.__valor

    @_valor.setter
    def _valor(self, value):
        self.__valor = value

    @property
    def _total(self):
        return self.__total

    @_total.setter
    def _total(self, value):
        self.__total = value

    def configurar_tela(self):
        self.tela.title("Calculo Produto")
        self.tela.configure(background="#f1f1f1")

        largura = 500
        altura = 420

        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()

        posx = largura_screen / 2 - largura / 2
        posy = altura_screen / 2 - altura / 2

        self.tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

    def criar_componentes(self):
        self.frame = Frame(self.tela, bg="#333", padx=20, pady=20)
        self.frame.pack(expand=True)

        self.titulo = Label(self.frame, text="CALCULO TOTAL PRODUTO", bg="#333", fg="white", font=("Arial", 14, "bold"))
        self.titulo.grid(row=0, column=0, columnspan=2, pady=10)

        Label(self.frame, text="Nome Produto:", bg="#333", fg="white", font="Arial").grid(row=1, column=0, sticky="w", pady=5)
        self.txt_nome = Entry(self.frame, width=35, bg="#ecf0f1")
        self.txt_nome.grid(row=1, column=1, pady=5)

        Label(self.frame, text="Quantidade Comprada:", bg="#333", fg="white", font="Arial").grid(row=2, column=0, sticky="w", pady=5)
        self.txt_qtd = Entry(self.frame, width=35, bg="#ecf0f1")
        self.txt_qtd.grid(row=2, column=1, pady=5)

        Label(self.frame, text="Preço Produto:", bg="#333", fg="white", font="Arial").grid(row=3, column=0, sticky="w", pady=5)
        self.txt_valor = Entry(self.frame, width=35, bg="#ecf0f1")
        self.txt_valor.grid(row=3, column=1, pady=5)

        Label(self.frame, text="Total Produto:", bg="#333", fg="white", font="Arial").grid(row=4, column=0, sticky="w", pady=5)
        self.txt_total = Entry(self.frame, width=35, bg="#ecf0f1")
        self.txt_total.grid(row=4, column=1, pady=5)

        self.lbl_dados = Label(self.frame, text="", bg="white", font=("Arial", 10), justify=CENTER, width=40, pady=8)
        self.lbl_dados.grid(row=5, column=0, columnspan=2, pady=8)

        self.btn_calcular = Button(self.frame, text="Total", font=("Arial", 10, "bold"), command=self.calcular)
        self.btn_calcular.grid(row=6, column=0, columnspan=2, pady=10)

    def calcular(self):
        self.__nome = self.txt_nome.get()
        self.__quantidade = int(self.txt_qtd.get())
        self.__valor = float(self.txt_valor.get())
        self.__total = self.__quantidade * self.__valor

        self.txt_total.delete(0, END)
        self.txt_total.insert(0, f"{self.__total:.2f}")

        self.mostrarDadosProduto()

    def mostrarDadosProduto(self):
        dados = (f"O produto: {self.__nome}\n Preço: {self.__valor:.2f}\n Quantidade: {self.__quantidade}\n\n Total: {self.__total:.2f}")
        self.lbl_dados.config(text=dados)

    def executar(self):
        self.tela.mainloop()
