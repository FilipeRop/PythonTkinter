from tkinter import *

global tempo
global rodar
global contador
global limitador

tempo = '00:00:00'
rodar = False
contador = -5
limitador = 59

#inicia a contagem
def iniciar():
    global rodar

    rodar = True
    Contagem()

def Contagem():
    global tempo 
    global contador
    global limitador

    if rodar:
        #pré contagem
        if contador <=-1:
            inicio = 'Começando em' + str(contador)
            label_tempo['text'] = inicio
            label_tempo['font'] = 'Arial 10'
        #início da contagem
        else:  
            label_tempo['font'] = 'Times 50 bold'
            valTemporaria = str(tempo)
            horas,minutos,segundos = map(int,valTemporaria.split(':'))
            horas = int(horas)
            minutos = int(minutos)
            segundos = int(contador)

            if (segundos >= limitador):
                contador = 0
                minutos += 1

            segundos = str(0) + str(segundos)
            minutos = str(0) + str(minutos)
            horas = str(0) + str(horas)

            #atualizando valores 
            valTemporaria = str(horas[-2:])+':'+str(minutos[-2:])+':'+str(segundos[-2:])
            label_tempo['text'] = valTemporaria
            tempo = valTemporaria

        label_tempo.after(1000, Contagem)    
        contador+=1

#função pausar
def pausar():
    global rodar
    rodar = False

#função reiniciar
def reiniciar():
    global tempo
    global contador 

    tempo = '00:00:00'
    contador = 0

    label_tempo['text'] = tempo

#cores
cor_fundo = '#000000' #preto
cor_fonte = '#ffffff' #branco
cor_botao = '#8f8f8f' #cinza

#configurando janela---------------------------
janela = Tk()
janela.title('')
janela.config(bg=cor_fundo)
janela.resizable(height=FALSE,width=FALSE)
janela.iconphoto(False, PhotoImage(file='midias\cronometro.png'))
janela.geometry('290x180')

#criando labels---------------------------
label_nomeApp = Label(janela, text='CRONÔMETRO', font=('Arial 10'), bg=cor_fundo, fg=cor_fonte)
label_nomeApp.place(x=20,y=5)

label_tempo = Label(janela, text=tempo, font=('Times 50 bold'), bg=cor_fundo, fg=cor_fonte)
label_tempo.place(x=20,y=30)

#criando botões----------------------------
botao_iniciar = Button(janela, command=iniciar, text='INICIAR', width=10, bg=cor_botao, relief='raised', overrelief='ridge')
botao_iniciar.place(x=20,y=130)

botao_pausar = Button(janela, command=pausar, text='PAUSAR', width=10, bg=cor_botao, relief='raised', overrelief='ridge')
botao_pausar.place(x=105,y=130)

botao_reiniciar = Button(janela, command=reiniciar, text='REINICIAR', width=10, bg=cor_botao, relief='raised', overrelief='ridge')
botao_reiniciar.place(x=190,y=130)

janela.mainloop()