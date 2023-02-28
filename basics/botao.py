from tkinter import *

janela = Tk()
janela.title('Minha janela')
janela.geometry('500x500')

global cont
cont = 0

def executar():
    global cont

    texto_1 = 'Número impar: '
    texto_2 = 'Número par: '

    if cont % 2 == 0:
        resultado = texto_2 + str(cont)
        label['text'] = resultado
        label['fg'] = 'green'
    else:
        resultado = texto_1 + str(cont)
        label['text'] = resultado
        label['fg'] = 'blue'

    cont += 1

botao = Button(janela, command=executar, text='Clique Aqui', relief='raised', bg='#40c7b0') #parâmetro relif referente a estilos, parâmetro command executa ações dentro do botão. 
#existem parâmetros que não  precisam ser necessariamente preechidos, tais como: width e height.
botao.place(x=10,y=10)

label = Label(janela, text='Não clique aqui', bg='#a361c2')
label.place(x=10,y=50)

janela.mainloop()

'''Outros estilos de botão: groove, solid, raised, sunken, ridge'''