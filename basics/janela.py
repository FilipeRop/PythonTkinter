from tkinter import *

#definindo cores
cor1 = '#b4bad6'
cor2 = '#2a2d3b'
cor3 = '#ab609c'

janela = Tk() #cria uma instância
janela.title('Minha Janela') #define o título da janela
janela.geometry('600x300') #define largura e altura
janela.config(bg=cor3) #define a cor de fundo

janela.iconphoto(False, PhotoImage(file='midias\logo.png')) #modifica o ícone
janela.resizable(width=False, height='False') #bloquear redimensionamento de tela

janela.mainloop() #garante o funcionamento 