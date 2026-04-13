from tkinter import *

class Calculo_Velocidade:
    def __init__(self):
        self.tela = Tk()
        self.configurar_tela()
        self.criar_componentes()

        # Atributos Privados
        self.__nome = ""
        self.__distancia = 0.0
        self.__tempo = 0.0
        self.__velocidade = 0.0

    @property
    def _nome(self):
        return self.__nome

    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _distancia(self):
        return self.__distancia

    @_distancia.setter
    def _distancia(self, value):
        self.__distancia = value

    @property
    def _tempo(self):
        return self.__tempo

    @_tempo.setter
    def _tempo(self, value):
        self.__tempo = value

    @property
    def _velocidade(self):
        return self.__velocidade

    @_velocidade.setter
    def _velocidade(self, value):
        self.__velocidade = value

    def configurar_tela(self):
        self.tela.title("Calculo Velocidade")
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

        self.titulo = Label(self.frame, text="VELOCIDADE CARRO",
                            bg="#333", fg="white",
                            font=("Arial", 14, "bold"))
        self.titulo.grid(row=0, column=0, columnspan=2, pady=10)

        Label(self.frame, text="Nome Carro:", bg="#333", fg="white",
              font="Arial").grid(row=1, column=0, sticky="w", pady=5)
        self.txt_nome = Entry(self.frame, width=35, bg="#ecf0f1")
        self.txt_nome.grid(row=1, column=1, pady=5)

        Label(self.frame, text="Distância Percorrida em Km:", bg="#333", fg="white",
              font="Arial").grid(row=2, column=0, sticky="w", pady=5)
        self.txt_distancia = Entry(self.frame, width=20, bg="#ecf0f1")
        self.txt_distancia.grid(row=2, column=1, pady=5)

        Label(self.frame, text="Tempo em minutos:", bg="#333", fg="white",
              font="Arial").grid(row=3, column=0, sticky="w", pady=5)
        self.txt_tempo = Entry(self.frame, width=20, bg="#ecf0f1")
        self.txt_tempo.grid(row=3, column=1, pady=5)

        Label(self.frame, text="Velocidade do Carro:", bg="#333", fg="white",
              font="Arial").grid(row=4, column=0, sticky="w", pady=5)
        self.txt_veloc = Entry(self.frame, width=20, bg="#ecf0f1")
        self.txt_veloc.grid(row=4, column=1, pady=5)

        self.lbl_resultado = Label(self.frame, text="", bg="white",
                                   font=("Arial", 10), justify=CENTER,
                                   width=40, pady=8)
        self.lbl_resultado.grid(row=5, column=0, columnspan=2, pady=8)

        self.btn_calcular = Button(self.frame, text="Calcular Velocidade",
                                   font=("Arial", 10, "bold"),
                                   command=self.calcularVelocidade)
        self.btn_calcular.grid(row=6, column=0, columnspan=2, pady=10)

    def calcularVelocidade(self):
        self.__nome = self.txt_nome.get()
        self.__distancia = float(self.txt_distancia.get())
        self.__tempo = float(self.txt_tempo.get())
        # distancia (km) * 1000 = metros; tempo (min) * 60 = segundos
        self.__velocidade = (self.__distancia * 1000) / (self.__tempo * 60)

        self.txt_veloc.delete(0, END)
        self.txt_veloc.insert(0, f"{self.__velocidade:.2f}")

        self.mostrarResultado()

    def mostrarResultado(self):
        dist_m = self.__distancia * 1000
        tempo_s = self.__tempo * 60
        dados = (f"O carro: {self.__nome}\n"
                 f"Percorreu: {dist_m:.0f} metros\n"
                 f"Em um tempo de: {tempo_s:.0f} segundos\n\n"
                 f"Velocidade: {self.__velocidade:.2f} m/s")
        self.lbl_resultado.config(text=dados)

    def executar(self):
        self.tela.mainloop()
