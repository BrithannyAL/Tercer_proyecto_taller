"""import cargar
from datetime import datetime
import control
import proyecto3
from time import sleep
import objetos

estado_reporte_emociones = True

def tomar_foto():
    mi_rostro=proyecto3.rostro()
    mi_rostro.capturar_imagen(vista=False)

def guardar_reporte_emociones(usuario, actividad, hora_i, hora_f, hora_actual):
    global estado_reporte_emociones
    reporte_emociones = []
    while (hora_i < datetime.now().time() < hora_f): 
        reporte_emociones.append(control.detectar_emociones())
        print(reporte_emociones)
        tomar_foto()
        sleep(1)
    dicc = {'Primeros cinco minutos' : reporte_emociones[:5],
            'Ultimos cinco minutos' : reporte_emociones[:-5]}
    linea = objetos.emociones(usuario, actividad, dicc)
    linea.guardar_en_archivos()
    print(linea)
    
tomar_foto()
    
hora_actual = datetime.now().time()    
hora_i = datetime.strptime('15:00:00', "%X").time()
hora_f = datetime.strptime('16:31:00', "%X").time()

guardar_reporte_emociones('barguello', 'Actividad de prueba', hora_i, hora_f, hora_actual)"""

import proyecto3

def tomar_foto():
    mi_rostro=proyecto3.rostro()
    mi_rostro.capturar_imagen(vista=False)

tomar_foto()