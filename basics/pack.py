from tkinter import *

cor ='#b4bad7'

janela = Tk()
janela.title('Place')
janela.geometry('300x300')
janela.config(bg = cor)

label_nome = Label(janela, width=10, height=2, text='NOME:', font=('Arial 10'), fg='white', bg='black')
label_nome.pack() #posiciona o widget em função do alinhamento

nome = Label(janela, width=10, height=2, text='Filipe', font=('Arial 10'), fg='white', bg='black')
nome.pack()

label_idade = Label(janela, width=10, height=2, text='IDADE:', font=('Arial 10'), fg='white', bg='black')
label_idade.pack()

idade = Label(janela, width=10, height=2, text='21', font=('Arial 10'), fg='white', bg='black')
idade.pack()

label_pais = Label(janela, width=10, height=2, text='PAÍS:', font=('Arial 10'), fg='white', bg='black')
label_pais.pack(side=LEFT)

pais = Label(janela, width=10, height=2, text='Brasil', font=('Arial 10'), fg='white', bg='black')
pais.pack(side=RIGHT)

janela.mainloop()