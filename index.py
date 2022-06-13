import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time
from datetime import datetime
import cargar
from hilo_ejecucion import hilo

root = tk.Tk()
root.title('Proyecto Taller')
root.minsize(800,600)


def curso_actual():
    global after_id
    global secs
    secs += 1
    usuario_data = cargar.cargar_archivos_usuario()
    dia_actual = datetime.today().strftime('%A')
    for i in usuario_data[8][dia_actual]:
        hora_i = datetime.strptime(i[1], "%X").time()
        hora_f = datetime.strptime(i[2], "%X").time()
        hora_actual = datetime.now().time()
        if hora_actual >= hora_i and hora_actual <= hora_f:
            actividad_actual = i
        else:
            actividad_actual = None
    if secs % 2 == 0:  # every other second
        print('encendido')
        import proyecto3
        imagen = proyecto3.rostro()
        imagen.capturar_imagen(vista=False)
        print(actividad_actual)
    after_id = root.after(1000, curso_actual)   #1000 = 1 segundo   #60000 = 1 minuto   #300000 = 5 minutos 


def hide(x):
    for i in x:
        i.pack_forget()

def show(x):
    for i in x:
        i.pack()

FREQ = 2500
DUR = 150
after_id = None
secs = 0

def encender():
    hilo(True)
    global secs
    secs = 0
    proceso.start()
    curso_actual()  # start repeated checking

def apagar():
    hilo(False)
    global after_id
    proceso._stop()
    if after_id:
        root.after_cancel(after_id)
        after_id = None

#Botones pantalla principal

btn_iniciar = tk.Button(root,text = 'Iniciar',width=8)
btn_iniciar.pack()

btn_detener = tk.Button(root,text='Detener',width=8)
btn_detener.pack()

btn_salir = tk.Button(root,text = 'Salir',width=8)
btn_salir.pack()

lbl_ejecucion = tk.Label(root, text=('Programa en ejecucion'))

#CONFIGURACIÓN DE LOS BOTONES DE LA PANTALLA DE INICIO
btn_iniciar.configure(command=lambda:
    [messagebox.showinfo(message='El programa está en ejecución'),lbl_ejecucion.pack(),encender()])

btn_detener.configure(command=lambda:
    [lbl_ejecucion.pack_forget(), apagar()])

btn_salir.configure(command = root.destroy)


tk.mainloop()