from tkinter import *
#Criando Tela do Tkinter - Interface Gráfica
tela = Tk()

#titulo
tela.title("Fatec Registro")

#cor de fundo
tela.configure(background="#3dd44c")
#tamanho tela
tela.geometry("700x500")

#redimensionar tela true ou false
tela.resizable(True, True)
#tamanho minimo
tela.minsize(width=400, height=600)
#tamanho maximo
tela.maxsize(width=700, height=800)

#CRIANDO LABEL
lbl_texto = Label(tela,text="Digite seu nome: ", background="#002000", foreground="#ffffff").place(x=10, y=20)
lbl_tel = Label(tela,text="Digite seu telefone: ", bg="#002000", fg="#FFFFFF", font={"Arial", "16", "bold", "italic"}).place(x=10, y=60)

# CRIANDO CAIXA DE TECTO
txt_nome = Entry(tela, width=50, borderwidth=3, bg= "white", fg="blue")
txt_nome.place(x=120, y=20)

txt_tel = Entry(tela, width=20, borderwidth=3, bg="white", fg="blue")
txt_tel.place(x=230, y=60)

def mostrardados():
    lbl_mostra = Label (tela, text= "Bem vindo " + txt_nome.get() + " Telefone: " + txt_tel.get())
    lbl_mostra.place(x=100, y = 150)

# CRIANDO BOTAO
btn_botao = Button(tela, text="Mostrar Dados", command=mostrardados)
btn_botao.place(x=160, y=100)


#Executar a Tela
tela.mainloop()