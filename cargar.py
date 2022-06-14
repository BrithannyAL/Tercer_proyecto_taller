from tkinter.messagebox import askyesno  
from objetos import  emociones

def cargar_archivos_usuario():
    global usuario
    respuesta = None
    try:
        with open("usuario.dat", "tr") as lector:
            lectura = eval(lector.readline()[:-1])
            if lectura != '':
                respuesta = lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5]
            lectura = eval(lector.readline()[:-1])    
            while (lectura != ''):
                respuesta.insertar(usuario(lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5]))
                lectura = eval(lector.readline()[:-1])      
    except FileNotFoundError as error:
        respuesta = askyesno(title="Error", message="No se encontró el archivo de datos ¿Desea crear un nuevo archivo de registros?")
        if respuesta:
            open("usuario.dat", "tw").close()
    finally:
        return respuesta
    
def cargar_archivos_emociones():
    global emociones
    respuesta = None
    try:
        with open("emociones.dat", "tr") as lector:
            lectura = eval(lector.readline()[:-1])
            if lectura != '':
                respuesta = lectura[0], lectura[1], lectura[2]
            lectura = eval(lector.readline()[:-1])    
            while (lectura != ''):
                respuesta.insertar(usuario(lectura[0], lectura[1], lectura[2]))
                lectura = eval(lector.readline()[:-1])      
    except FileNotFoundError as error:
        respuesta = askyesno(title="Error", message="No se encontró el archivo de datos ¿Desea crear un nuevo archivo de registros?")
        if respuesta:
            open("emociones.dat", "tw").close()
    finally:
        return respuesta