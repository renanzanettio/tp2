from tkinter import *

class Clientes:
    def __init__(self):
        self.tela = Tk()
        self.configurar_tela()
        self.criar_componentes()

        # Atributos Privados
        self.__nome = ""
        self.__email = ""
        self.__telefone = ""
        self.__endereco = ""

    @property
    def _nome(self):
        return self.__nome

    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _email(self):
        return self.__email

    @_email.setter
    def _email(self, value):
        self.__email = value

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

    def configurar_tela(self):
        self.tela.title("Cadastro de Clientes")
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

        self.titulo = Label(self.frame, text="CADASTRO DE CLIENTES", bg="#333", fg="white", font=("Arial", 14, "bold"))
        self.titulo.grid(row=0, column=0, columnspan=2, pady=10)

        Label(self.frame, text="Nome:", bg="#333", fg="white", font="Arial").grid(row=1, column=0, sticky="w", pady=5)
        self.txt_nome = Entry(self.frame, width=35, bg="#ecf0f1")
        self.txt_nome.grid(row=1, column=1, pady=5)

        Label(self.frame, text="E-mail:", bg="#333", fg="white", font="Arial").grid(row=2, column=0, sticky="w", pady=5)
        self.txt_email = Entry(self.frame, width=35, bg="#ecf0f1")
        self.txt_email.grid(row=2, column=1, pady=5)

        Label(self.frame, text="Telefone:", bg="#333", fg="white", font="Arial").grid(row=3, column=0, sticky="w", pady=5)
        self.txt_telefone = Entry(self.frame, width=35, bg="#ecf0f1")
        self.txt_telefone.grid(row=3, column=1, pady=5)

        Label(self.frame, text="Endereço:", bg="#333", fg="white", font="Arial").grid(row=4, column=0, sticky="w", pady=5)
        self.txt_endereco = Entry(self.frame, width=35, bg="#ecf0f1")
        self.txt_endereco.grid(row=4, column=1, pady=5)

        self.btn_cadastrar = Button(self.frame, text="Cadastrar Cliente", font=("Arial", 10, "bold"), command=self.cadastrarCliente)
        self.btn_cadastrar.grid(row=5, column=0, columnspan=2, pady=15)

        self.lbl_dados = Label(self.frame, text="", bg="white", font=("Arial", 10), justify=CENTER, width=40, pady=8)
        self.lbl_dados.grid(row=6, column=0, columnspan=2, pady=5)

    def cadastrarCliente(self):
        self.__nome = self.txt_nome.get()
        self.__email = self.txt_email.get()
        self.__telefone = self.txt_telefone.get()
        self.__endereco = self.txt_endereco.get()
        self.mostrarDados()

    def mostrarDados(self):
        dados = (f"Nome: {self.__nome}\n E-mail: {self.__email}\n Telefone: {self.__telefone}\n Endereço: {self.__endereco}")
        self.lbl_dados.config(text=dados)

    def executar(self):
        self.tela.mainloop()
