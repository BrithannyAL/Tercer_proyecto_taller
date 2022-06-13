from proyecto3 import rostro
import threading
from time import sleep 
from  control import detectar_concentracion, detectar_emociones      

#variables globales

def tarea_paralela():
    mi_rostro=rostro()
    while estado[0]==True:
        mi_rostro.capturar_imagen(vista=False)
        detectar_concentracion()
        detectar_emociones()

estado=[True]
parametros=[estado]
proceso=threading.Thread(target=tarea_paralela, args=parametros)