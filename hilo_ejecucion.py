from proyecto3 import rostro
import threading
from time import sleep 
from  control import detectar_concentracion, detectar_emociones   
import cargar
from objetos import usuario, emociones   
from datetime import datetime
from statistics import mode

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
    print(hora_i)
    print(hora_f)
    while (hora_i < datetime.now().time() < hora_f) and (estado_tarea_emociones == True): 
        reporte_emociones.append(detectar_emociones())
        print(reporte_emociones)
        tomar_foto()
        sleep(1)
        
    emociones_pcinco = []
    emociones_ucinco = []
    emociones_data = cargar.cargar_archivos_emociones()
        
    for x in emociones_data.emociones['Primeros cinco minutos']:
        for y in x:
            emociones_pcinco.append(y)  
            
    for x in emociones_data.emociones['Ultimos cinco minutos']:
        for y in x:
            emociones_ucinco.append(y)  
            
    lista_emocion_dominante = emociones_pcinco + emociones_ucinco
    
    try:    
        dicc = {'Primeros cinco minutos' : mode(emociones_pcinco),
                'Ultimos cinco minutos' : mode(emociones_ucinco),
                'Emoción dominante' : mode(lista_emocion_dominante)}
    except:
        dicc = {'Primeros cinco minutos' : 'El usuario experientó muchos cambios de emociones',
                'Ultimos cinco minutos' : 'El usuario experientó muchos cambios de emociones',
                'Emoción dominante' : 'No hay emoción dominante'}
    
    emociones_data.insertar(emociones(usuario, actividad_actual, dicc))
    emociones_data.guardar_en_archivos()

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
    

