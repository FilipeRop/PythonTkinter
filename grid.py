from tkinter import *

cor ='#b4bad7'

janela = Tk()
janela.title('Place')
janela.geometry('300x300')
janela.config(bg = cor)

label_nome = Label(janela, width=10, height=2, text='NOME:', font=('Arial 10'), fg='white', bg='black')
label_nome.grid(row=0,column=0, padx=5, pady=5) #posiciona o widget em fução de linhas e colunas

nome = Label(janela, width=10, height=2, text='Filipe', font=('Arial 10'), fg='white', bg='black')
nome.grid(row=0,column=1)

label_idade = Label(janela, width=10, height=2, text='IDADE:', font=('Arial 10'), fg='white', bg='black')
label_idade.grid(row=1,column=0, padx=5, pady=5)

idade = Label(janela, width=10, height=2, text='21', font=('Arial 10'), fg='white', bg='black')
idade.grid(row=1,column=1, padx=5, pady=5)

label_pais = Label(janela, width=10, height=2, text='PAÍS:', font=('Arial 10'), fg='white', bg='black')
label_pais.grid(row=2,column=0, padx=5, pady=5)

pais = Label(janela, width=10, height=2, text='Brasil', font=('Arial 10'), fg='white', bg='black')
pais.grid(row=2,column=1)

janela.mainloop()