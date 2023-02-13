from tkinter import	 *

janela = Tk()

janela.title('Label')
janela.geometry('500x500')
janela.config(bg='#b4bad6')
janela.resizable(width=False, height=False)

label_nome = Label(janela, width=10, height=2, text='Nome: ', font=('Arial 12'), fg='#c24940', bg='#000000') #define o label e seus parâmetros
label_nome.grid(row=0, column=0, pady=10) #define a posição do label

label_idade = Label(janela, width=10, height=2, text='Idade: ', font=('Arial 12 bold'), fg='#c240b9', bg='#000000')
label_idade.grid(row=1, column=0, pady=10)

label_pais = Label(janela, width=10, height=2, text='País: ', font=('Arial 12'), fg='#65c240')
label_pais.grid(row=2, column=0, pady=10)

janela.mainloop()
