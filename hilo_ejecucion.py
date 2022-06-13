from proyecto3 import rostro
import threading
from time import sleep 
from  control import detectar_concentracion, detectar_emociones      

#variables globales

def tarea_paralela(estado):
    mi_rostro=rostro()
    while estado[0]==True:
        mi_rostro.capturar_imagen(vista=False)
        detectar_concentracion()
        detectar_emociones()
        
def hilo(respuesta):
    estado=[respuesta]
    parametros=[estado]
    proceso=threading.Thread(target=tarea_paralela, args=parametros)
