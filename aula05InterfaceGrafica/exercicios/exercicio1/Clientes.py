from tkinter import *

class cadastrarCliente:
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
        self.tela.title("Aplicação O_O")
        self.tela.configure(background="#75B896")

        # Define o tamanho padrão da sua tela
        largura = 800
        altura = 300

        # Pega a largura e altura da tela do Windows
        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()

        # Define o posicionamento centralizado
        posx = largura_screen / 2 - largura / 2
        posy = altura_screen / 2 - altura / 2

        # Controi a tela de acordo com as dimensões da tela do Windows
        # %D Substitui cada número   % Concatena cada variavel largura, altura...
        self.tela.geometry("%dx%d+%d+%d" % (largura ,altura, posx , posy))

    def criar_componentes(self):
        # Criar frame
        self.frame = Frame(self.tela, bg= "#75B896", padx= 20, pady= 20)
        # Pack posiciona de acordo com a tela expand => ocupa espaço na tela ao redimensionar
        self.frame.pack(expand=True)

        # Titulo
        self.titulo = Label(self.frame, text="CADASTRO DE CLIENTES")

        # Grid => Cria grade    Row = linha   Colum= coluna
        #pady = espacamento parte de cima e de baixo de 10px
        self.titulo.grid(row=0, column= 0, columnspan= 2, padx= 10)

        # Nome
        # Sticky= "w" posicionamento do texto lado esquerdo (oeste)
        Label(self.frame, text="Digite o nome:").grid(row= 1, column= 0, sticky= "w", pady= 5)

        self.txt_nome = Entry(self.frame)
        self.txt_nome.grid(row= 1, column= 1, pady= 5)

        # Email
        Label(self.frame, text="Digite o email:").grid(row= 3, column= 0, sticky= "w", pady= 5)

        self.txt_email = Entry(self.frame)
        self.txt_email.grid(row= 3, column= 1, pady= 5)

        # Telefone
        Label(self.frame, text="Digite o telefone:").grid(row= 5, column= 0, sticky= "w", pady= 5)

        self.txt_telefone = Entry(self.frame)
        self.txt_telefone.grid(row= 5, column= 1, pady= 5)

        # Endereço
        Label(self.frame, text="Digite o endereço:").grid(row= 7, column= 0, sticky= "w", pady= 5)

        self.txt_endereco = Entry(self.frame)
        self.txt_endereco.grid(row= 7, column= 1, pady= 5)

        # Mostrar Dados
        Label(self.frame, text="Dados Do Cliente:", font=18, bg="#75B896").grid(row= 8, column= 1, sticky= "w", pady= 5)

        self.txt_resul = Entry(self.frame, bg="#ffffff")
        self.txt_resul.grid(row= 9, column= 1, columnspan=2, pady= 5)

        #BOTAO
        self.btn_botao = Button(self.frame, text="Cadastrar Cliente", command= self.mostrarDados)
        self.btn_botao.grid(row= 10, column= 0, columnspan= 2, rowspan=2, pady= 15)

    def mostrarDados(self):
        # Recebendo os valores caixas de texto e guardando atributos
        self.txt_formatado = f"Nome: {self.txt_nome.get()} \n Email: {self.txt_email.get()} \n Telefone: {self.txt_telefone.get()} \n Endereço: {self.txt_endereco.get()}"

        # Pegando o resultado da soma e jogando na caixinha de texto
        self.txt_resul.insert(0, self.txt_formatado)

    def executar(self):
        self.tela.mainloop()


