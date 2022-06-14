from proyecto3 import rostro
import threading
from time import sleep 
from  control import detectar_concentracion, detectar_emociones      

#variables globales

def tarea_paralela():
    mi_rostro=rostro()
    mi_rostro.capturar_imagen(vista=False)
    detectar_concentracion()
    detectar_emociones()




 



