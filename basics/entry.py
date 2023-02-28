from tkinter import *

janela = Tk()
janela.title('Minha Janela')
janela.geometry('500x500')

#função obter------------------------------

def obter():
    nome = entry_nome.get()
    idade = entry_idade.get()
    pais = entry_pais.get()

    label_nome_resposta['text'] = nome
    label_idade_resposta['text'] = idade
    label_pais_resposta['text'] = pais

    entry_nome.delete(0,END) #limpa as entradas ao submeter
    entry_idade.delete(0,END)
    entry_pais.delete(0,END)


#nome--------------------------------------
label_nome = Label(janela, text='Nome: ') 
label_nome.grid(row=0, column=0, pady=10)
entry_nome = Entry(janela) #propriedade que define uma entrada
entry_nome.grid(row=0, column=1)

#idade-------------------------------------
label_idade = Label(janela, text='Idade: ') 
label_idade.grid(row=1, column=0, pady=10)
entry_idade = Entry(janela)
entry_idade.grid(row=1, column=1)

#país--------------------------------------
label_pais = Label(janela, text='País: ') 
label_pais.grid(row=2, column=0, pady=10)
entry_pais = Entry(janela, state='disabled') #desabilita entrada
entry_pais.grid(row=2, column=1)

#respostas---------------------------------
label_nome_resposta = Label(janela, text='') 
label_nome_resposta.grid(row=0, column=2, pady=10)

label_idade_resposta = Label(janela, text='') 
label_idade_resposta.grid(row=1, column=2, pady=10)

label_pais_resposta = Label(janela, text='') 
label_pais_resposta.grid(row=2, column=2, pady=10)

botao = Button(janela, command=obter, width=10, text='Entrar')
botao.grid(row=3, column=0)

janela.mainloop() 