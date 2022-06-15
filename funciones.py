import cargar
from statistics import mode

def obtener_reporte_emociones():
    lista_emociones = cargar.cargar_archivos_emociones()
    lista_emociones.sig
    print(lista_emociones.actividad)
    lista = []
    
    emocionesp = lista_emociones.emociones['Primeros cinco minutos']
    emocionesu = lista_emociones.emociones['Ultimos cinco minutos']
    emocionesd = lista_emociones.emociones['Emocion dominante']
    lista.append([lista_emociones.usuario, lista_emociones.actividad, emocionesp, emocionesu, emocionesd])
    
    while lista_emociones.sig != None:  
        emocionesp = lista_emociones.emociones['Primeros cinco minutos']
        emocionesu = lista_emociones.emociones['Ultimos cinco minutos']
        emocionesd = lista_emociones.emociones['Emocion dominante']
        lista.append([lista_emociones.usuario, lista_emociones.actividad, emocionesp, emocionesu, emocionesd])
        
    return lista

result = obtener_reporte_emociones()
print(result)

