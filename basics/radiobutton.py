from tkinter import *

janela=Tk()
janela.geometry('300x250')

def obter():
    resultado = selecionado_1.get()
    print(resultado)

selecionado_1 = IntVar() #criando variável auxiliar
selecionado_2 = StringVar()
selecionado_3 = BooleanVar()

radio_1 = Radiobutton(janela,command=obter, text='Primeiro', value=1, variable=selecionado_1) #definindo radiobutton e atribuindo valor na variável auxiliar
radio_1.grid(row=0,column=0)

radio_2 = Radiobutton(janela,command=obter, text='Segundo', value=2, variable=selecionado_1)
radio_2.grid(row=1,column=0)

radio_3 = Radiobutton(janela,command=obter, text='Terceiro', value=3, variable=selecionado_1)
radio_3.grid(row=2,column=0)

botao = Button()




janela.mainloop()