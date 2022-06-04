from email.mime import base
from cgitb import text
import tkinter as tk
from tkinter import ttk
from tkinter import *



ventana_login = tk.Tk()
ventana_login.title('Proyecto Taller')
ventana_login.minsize(800,600)

def hide(x):
    for i in x:
        i.pack_forget()

def show(x):
    for i in x:
        i.pack()


#Login



def ingresar(bl):
    if type(bl[0]) == int:
        if bl[0] == 1:
            pass
        elif bl[0] == 2:
            global u
            u = bl[1]
            pass

    else:
        return(generar_ventana_login())

def generar_ventana_login():
    sv_usuario = tk.StringVar()
    sv_contrasena = tk.StringVar()
        
    lb_usuario = tk.Label(ventana_login,text='Ingrese su nombre de usuario: ')
    e_usuario = ttk.Entry(ventana_login, textvariable = sv_usuario, width = 40)

    lb_contra = tk.Label(ventana_login,text='Ingrese su contraseña: ')
    e_contra = ttk.Entry(ventana_login,textvariable = sv_contrasena, width = 40)
    
    btn_ingresar = tk.Button(ventana_login,text = 'Ingresar')
    btn_ingresar.configure(command= lambda:
        [hide([lb_usuario, e_usuario, lb_contra, e_contra, btn_ingresar])])
    
    return(
        show([lb_usuario, e_usuario, lb_contra, e_contra, btn_ingresar])
    )


btn_login = tk.Button(ventana_login,text = 'Iniciar sesion')
btn_login.place(x=60,y=100)


btn_salir = tk.Button(ventana_login,text = 'Salir')
btn_salir.place(x=80,y=100)

#CONFIGURACIÓN DE LOS BOTONES DE LA PANTALLA DE INICIO
btn_login.configure(command=lambda:
    [hide([btn_salir,btn_login]), generar_ventana_login()])


btn_salir.configure(command = ventana_login.destroy)

btn_login.pack()
btn_salir.pack()










tk.mainloop()