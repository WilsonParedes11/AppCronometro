#-----Cronometro-----#
#-----@Wilson11-----#

from tkinter import *


#-----Configuracion de la GUI-----#

ventana = Tk()
ventana.config(bg='black')
ventana.geometry('500x250')
ventana.title('Cronometro')
ventana.minsize(width=500,height=250)

ventana.columnconfigure(0,weight=2)
ventana.rowconfigure(0,weight=2)
ventana.columnconfigure(1,weight=2)
ventana.rowconfigure(0,weight=2)
ventana.columnconfigure(2,weight=2)
ventana.rowconfigure(0,weight=2)
ventana.columnconfigure(1,weight=2)
ventana.rowconfigure(1,weight=1)
ventana.columnconfigure(1,weight=2)
ventana.rowconfigure(1,weight=1)

#-----Codificacion de Frames internos-----#

frame1 = Frame(ventana)
frame1.grid(column=0,row=0,sticky='snew')

frame2 = Frame(ventana)
frame2.grid(column=1,row=0,sticky='snew')

frame3 = Frame(ventana)
frame3.grid(column=2,row=0,sticky='snew')

frame4 = Frame(ventana,bg='gray10')
frame4.grid(columnspan=3,row=1,sticky='snew')

frame5 = Frame(ventana, bg='black')
frame5.grid(columnspan=3,row=2,sticky='snew')

frame1.columnconfigure(0,weight=1)
frame1.rowconfigure(0,weight=1)
frame2.columnconfigure(0,weight=1)
frame2.rowconfigure(0,weight=1)
frame3.columnconfigure(0,weight=1)
frame3.rowconfigure(0,weight=1)
frame4.columnconfigure(0,weight=1)
frame4.rowconfigure(0,weight=1)
frame5.columnconfigure(0,weight=1)
frame5.rowconfigure(0,weight=1)

canvas1 = Canvas(frame1, bg='gray40', width=200, height=200, highlightthickness=0)
canvas1.grid(column=0,row=0,sticky='nsew')
canvas2 = Canvas(frame2, bg='gray30',width=200, height=200, highlightthickness=0)
canvas2.grid(column=0, row=0, sticky='nsew')
canvas3 = Canvas(frame3, bg='gray20',width=200, height=200, highlightthickness=0)
canvas3.grid(column=0, row=0,sticky='nsew')

texto1 = canvas1.create_text(1,1, text='0', font=('Arial',12,'bold'), fill='white')
texto2 = canvas2.create_text(1,1, text='0', font=('Arial',12,'bold'), fill='white')
texto3 = canvas3.create_text(1,1, text='0', font=('Arial',12,'bold'), fill='white')

texto_menutos = canvas1.create_text(1,1, text='Minutos', font=('Arial',12,'bold'),fill='white', justify='center')
texto_segundos = canvas2.create_text(1,1, text='Segundos', font=('Arial',12,'bold'),fill='white', justify='center')
texto_milisegundos = canvas3.create_text(1,1, text='Milisegundos', font=('Arial',12,'bold'),fill='white', justify='center')

circulo1 = canvas1.create_oval(10,10,100,100, outline='#006400', width=10)
circulo2 = canvas2.create_oval(10,10,100,100, outline='#006400', width=10)
circulo3 = canvas3.create_oval(10,10,100,100, outline='#006400', width=10)



ventana.mainloop()