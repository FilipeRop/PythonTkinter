from tkinter import *
from tkinter.ttk import *
janela = Tk()
janela.title('ComboBox')
janela.geometry('500x300')

label_nome = Label(janela, text='Escolha um item')
label_nome.grid(row=0,column=0)

def obter(): #função para retornar uma resposta da combobox
    resultado = combo.get()
    print(resultado)

combo = Combobox(janela) #criando combobox
combo['values'] = (1,2,3,4,5,'Filipe','Lima') #definindo valores
combo.current(1) #define um índice para valor inicial
combo.grid(row=1,column=0)

botao = Button(janela, command=obter, text='Ver resposta')
botao.grid(row=2, column=0)

janela.mainloop()