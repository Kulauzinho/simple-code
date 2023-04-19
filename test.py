import random
from tkinter import *
from tkinter import ttk

escolha = ['papel', 'pedra', 'tesoura']
computador = random.choice(escolha)
player = None

class pedra_fun():
    def __init__(self):
        self.pedra_func()
    def pedra_func(self):
        player = 'pedra'
        
class papel_fun():
    def __init__(self):
        self.papel_func()
    def papel_func(self):
        player = 'papel'
        
class tesoura_fun():
    def __init__(self):
        self.tesoura_func()
    def tesoura_func(self):
        player = 'tesoura'
       
root = Tk()

class janela():
    def __init__(self): #definição inicial para tudo dentro da classe funcionar
        self.root = root #equivalencia para que as outras 'defs' funcionem
        self.window() #validar as definições dentro de 'def window'
        self.buttons()
        self.texts()
        self.mensagem()
        root.mainloop() #manter a janela aberta
    def window(self):
        self.root.configure(background= '#F5F5F5')
        self.root.geometry('600x400')
        self.root.resizable(False, False)
        self.root.title('JoKenPô')
    def buttons(self):
        self.pedra = Button(text="Pedra", bd=4, command= pedra_fun)
        self.pedra.place(relx= 0.1, rely= 0.25, relwidth= 0.12, relheight= 0.09)
        self.papel = Button(text="Papel", bd=4, command= papel_fun)
        self.papel.place(relx= 0.4, rely=0.25, relwidth= 0.12, relheight= 0.09)
        self.tesoura = Button(text="Tesoura", bd=4, command= tesoura_fun)
        self.tesoura.place(relx= 0.7, rely=0.25, relwidth= 0.12, relheight= 0.09)
    def texts(self):
        self.texto_1 = Label(text='Escolha sua Opção:', font= '10')
        self.texto_1.place(relx= 0.35, rely= 0.1 )
        self.texto_2 = Label(text= 'Resultado:', font= '10')
        self.texto_2.place(relx= 0.4, rely= 0.5)
    def mensagem(self):
        self.mensagem = ttk.Treeview(height= 4, columns=('col1'))
        self.mensagem.place(relx= 0.33, rely= 0.6, relheight=0.1, relwidth= 0.3 )
        self.mensagem.column('#1', width=50)
        
   
janela() #manter a janela aberta