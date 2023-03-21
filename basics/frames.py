from tkinter import *

janela=Tk()
janela.title('Frames')
janela.geometry('400x400')

frame_1 = Frame(janela, width=200, height=200, bg='blue') #criando frame
frame_1.grid(row=0,column=0)

frame_2 = Frame(janela, width=200, height=200, bg='red')
frame_2.grid(row=1,column=0)

frame_3 = Frame(janela, width=200, height=200, bg='yellow')
frame_3.grid(row=1,column=1)

frame_4 = Frame(janela, width=200, height=200, bg='green')
frame_4.grid(row=0,column=1)

frame_5 = Frame(frame_1, width=20, height=20, bg='black')
frame_5.grid(row=0,column=0)

janela.mainloop()