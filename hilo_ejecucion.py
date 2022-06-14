from proyecto3 import rostro
import threading
from time import sleep 
from  control import detectar_concentracion, detectar_emociones   
import cargar
from objetos import usuario, emociones   
from datetime import datetime

#variables globales
estado_tarea_paralela = True
estado_tarea_emociones = True

def tarea_paralela():
    encender_tarea_emociones()
    global estado_tarea_paralela
    while estado_tarea_paralela == True:
        mi_rostro=rostro()
        mi_rostro.capturar_imagen(vista=False)
        detectar_concentracion()
        sleep(5)
    apagar_tarea_emociones()

proceso_control=threading.Thread(target=tarea_paralela)

def tomar_foto():
    mi_rostro=rostro()
    mi_rostro.capturar_imagen(vista=False)

def guardar_reporte_emociones():
    global estado_tarea_emociones
    
    usuario_data = cargar.cargar_archivos_usuario()
    actividad_actual = None
    usuario = usuario_data.usuario
    hora_i = None
    hora_f = None
    
    for x in usuario_data.actividades[datetime.today().strftime('%A')]:
        if  datetime.now().time() < datetime.strptime(x[2],"%X").time():
            hora_i = datetime.strptime(x[1],"%X").time()
            hora_f = datetime.strptime(x[2],"%X").time()
            actividad_actual = x[0]
    
    reporte_emociones = []
    print("JUSTO ANTES DEL WHILE")
    print(hora_i)
    print(hora_f)
    while (hora_i < datetime.now().time() < hora_f) and (estado_tarea_emociones == True): 
        print("YA ESTOY EN EL WHILE")
        reporte_emociones.append(detectar_emociones())
        print(reporte_emociones)
        tomar_foto()
        sleep(1)
        
    dicc = {'Primeros cinco minutos' : reporte_emociones[:5],
            'Ultimos cinco minutos' : reporte_emociones[-5:]}
    linea = emociones(usuario, actividad_actual, dicc)
    linea.guardar_en_archivos()
    print(linea)

proceso_emociones=threading.Thread(target=guardar_reporte_emociones)
 
def apagar_tarea_emociones():
    global proceso_emociones
    global estado_tarea_emociones
    estado_tarea_emociones = False
    proceso_emociones._stop()
    
def encender_tarea_emociones():
    global proceso_emociones
    proceso_emociones.start()
    
def apagar_tarea_paralela():
    global proceso_control
    global estado_tarea_paralela
    estado_tarea_paralela = False
    proceso_control._stop()
    
def encender_tarea_paralela():
    global proceso_emociones
    proceso_control.start()
    

