from proyecto3 import Rostro
import threading
from sonido import sonido
from time import sleep

def tarea_paralela(estado):
    mi_rostro=Rostro()
    while estado[0]:
        mi_rostro.capturar_imagen(vista=False,cuenta_regresiva=False)
        sonido()
        sleep(1)
        
def hilo_de_ejecucion():
    estado=[True]
    parametros=[estado]
    proceso=threading.Thread(target=tarea_paralela,args=parametros)
    proceso.start()

    variable = True
    while variable:
        respuesta = input('¿Desea terminar con la ejecución? (y/n)')
        if respuesta == 'y':
            estado[0]=False
            exit()
            variable = False
        elif  respuesta == 'n':
            print('El hilo sigue en ejecución')
        else:
            print('El caracter ingresado no tiene ninguna función')
        sleep(10)
            
hilo_de_ejecucion()