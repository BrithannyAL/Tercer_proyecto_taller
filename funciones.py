import cargar
from statistics import mode

def obtener_reporte_emociones():
    lista_emociones = cargar.cargar_archivos_emociones()
    lista = []
    
    emocionesp = lista_emociones.emociones['Primeros cinco minutos']
    emocionesu = lista_emociones.emociones['Ultimos cinco minutos']
    lista.append([lista_emociones.usuario, lista_emociones.actividad, emocionesp, emocionesu])
    
    while lista_emociones.sig != None:        
        emocionesp = lista_emociones.emociones['Primeros cinco minutos']
        emocionesu = lista_emociones.emociones['Ultimos cinco minutos']
        lista.append([lista_emociones.usuario, lista_emociones.actividad, emocionesp, emocionesu])
        
    return lista