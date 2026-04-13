from tkinter import *

class Contatos:
    def __init__(self):
        self.tela = Tk()
        self.configurar_tela()
        self.criar_componentes()

        # Atributos Privados
        self.__nome = ""
        self.__telefone = ""
        self.__endereco = ""
        self.__cidade = ""

    @property
    def _nome(self):
        return self.__nome

    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _telefone(self):
        return self.__telefone

    @_telefone.setter
    def _telefone(self, value):
        self.__telefone = value

    @property
    def _endereco(self):
        return self.__endereco

    @_endereco.setter
    def _endereco(self, value):
        self.__endereco = value

    @property
    def _cidade(self):
        return self.__cidade

    @_cidade.setter
    def _cidade(self, value):
        self.__cidade = value

    def configurar_tela(self):
        self.tela.title("Contatos")
        self.tela.configure(background="#f1f1f1")

        largura = 500
        altura = 400

        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()

        posx = largura_screen / 2 - largura / 2
        posy = altura_screen / 2 - altura / 2

        self.tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

    def criar_componentes(self):
        self.frame = Frame(self.tela, bg="#333", padx=20, pady=20)
        self.frame.pack(expand=True)

        self.titulo = Label(self.frame, text="CONTATOS", bg="#333", fg="white", font=("Arial", 14, "bold"))
        self.titulo.grid(row=0, column=0, columnspan=2, pady=10)

        Label(self.frame, text="Nome:", bg="#333", fg="white", font="Arial").grid(row=1, column=0, sticky="w", pady=5)
        self.txt_nome = Entry(self.frame, width=35, bg="#ecf0f1")
        self.txt_nome.grid(row=1, column=1, pady=5)

        Label(self.frame, text="Telefone:", bg="#333", fg="white", font="Arial").grid(row=2, column=0, sticky="w", pady=5)
        self.txt_telefone = Entry(self.frame, width=35, bg="#ecf0f1")
        self.txt_telefone.grid(row=2, column=1, pady=5)

        Label(self.frame, text="Endereço:", bg="#333", fg="white", font="Arial").grid(row=3, column=0, sticky="w", pady=5)
        self.txt_endereco = Entry(self.frame, width=35, bg="#ecf0f1")
        self.txt_endereco.grid(row=3, column=1, pady=5)

        Label(self.frame, text="Cidade:", bg="#333", fg="white", font="Arial").grid(row=4, column=0, sticky="w", pady=5)
        self.txt_cidade = Entry(self.frame, width=35, bg="#ecf0f1")
        self.txt_cidade.grid(row=4, column=1, pady=5)

        self.btn_dados = Button(self.frame, text="Dados do Contato", font=("Arial", 10, "bold"), command=self.cadastrarDados)
        self.btn_dados.grid(row=5, column=0, columnspan=2, pady=15)

        self.lbl_dados = Label(self.frame, text="", bg="white", font=("Arial", 10), justify=CENTER, width=40, pady=8)
        self.lbl_dados.grid(row=6, column=0, columnspan=2, pady=5)

    def cadastrarDados(self):
        self.__nome = self.txt_nome.get()
        self.__telefone = self.txt_telefone.get()
        self.__endereco = self.txt_endereco.get()
        self.__cidade = self.txt_cidade.get()
        self.mostrarDados()

    def mostrarDados(self):
        dados = (f"Nome: {self.__nome}\n Telefone: {self.__telefone}\n Endereço: {self.__endereco}\n Cidade: {self.__cidade}")
        self.lbl_dados.config(text=dados)

    def executar(self):
        self.tela.mainloop()
