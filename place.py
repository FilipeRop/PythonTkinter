from tkinter import *

cor ='#b4bad7'

janela = Tk()
janela.title('Place')
janela.geometry('300x300')
janela.config(bg = cor)

label_nome = Label(janela, width=10, height=2, text='NOME:', font=('Arial 10'), fg='white', bg='black')
label_nome.place(x=10,y=10) #posiciona o widget em função dos eixos X e Y

nome = Label(janela, width=10, height=2, text='Filipe', font=('Arial 10'), fg='white', bg='black')
nome.place(x=100,y=10)

label_idade = Label(janela, width=10, height=2, text='IDADE:', font=('Arial 10'), fg='white', bg='black')
label_idade.place(x=10,y=50)

idade = Label(janela, width=10, height=2, text='21', font=('Arial 10'), fg='white', bg='black')
idade.place(x=100,y=50)

label_pais = Label(janela, width=10, height=2, text='PAÍS:', font=('Arial 10'), fg='white', bg='black')
label_pais.place(x=10,y=90)

pais = Label(janela, width=10, height=2, text='Brasil', font=('Arial 10'), fg='white', bg='black')
pais.place(x=100,y=90)

janela.mainloop()