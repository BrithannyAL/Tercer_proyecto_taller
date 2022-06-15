import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time
from datetime import datetime
import cargar
import hilo_ejecucion
import os
import funciones
from tkinter import ttk
import graph
root = tk.Tk()
root.title('Proyecto Taller')
root.minsize(800,600)

listbox = tk.Listbox(root)

def crear_listbox(si):
    if si == 'si':
        
        lista = funciones.obtener_reporte_emociones()

        for x in lista:
            listbox.insert(END, f'Usuario: {x[0]}: Actividad: {x[1]} Primeros 5 {x[2]} Ultimos 5 {x[3]} Predominante {x[4]}')

        listbox.configure(height=15,selectmode='extended', width=120)
        listbox.pack()
        return listbox
    
    elif si == 'no':
        listbox.pack_forget()
        
        

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
global encendido 
encendido = int
def encender():
    hilo_ejecucion.encender_tarea_paralela()

def apagar():
    hilo_ejecucion.apagar_tarea_paralela()

#Botones pantalla principal

btn_iniciar = tk.Button(root,text = 'Iniciar',width=8)
btn_iniciar.pack()

btn_detener = tk.Button(root,text='Detener',width=8)
btn_detener.pack()

btn_reporte = tk.Button(root,text='Reporte',width=8)
btn_reporte.pack()

btn_salir = tk.Button(root,text = 'Salir',width=8)
btn_salir.pack()

cb = ttk.Combobox()
cb.pack()

actividad = list
x = cargar.cargar_archivos_emociones()
x.actividad

cb['values'] = (x.actividad)
btn_graph = tk.Button(root,text = 'Grafico',width=8)
btn_graph.pack()

btn_graph.configure(command = graph.crear_grafica(x.cantidades))

lbl_ejecucion = tk.Label(root, text=('Programa en ejecucion'))

#CONFIGURACIÓN DE LOS BOTONES DE LA PANTALLA DE INICIO
btn_iniciar.configure(command=lambda:
    [messagebox.showinfo(message='El programa está en ejecución'),lbl_ejecucion.pack(),encender()])

btn_detener.configure(command=lambda:
    [lbl_ejecucion.pack_forget(), apagar()])

btn_reporte.configure(command=lambda:  [crear_listbox('si')])

btn_salir.configure(command = root.destroy)


tk.mainloop()