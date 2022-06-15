import cargar
from statistics import mode

def obtener_reporte_emociones():
    lista_emociones = cargar.cargar_archivos_emociones()
    
    for x in lista_emociones.emociones['Primeros cinco minutos']:
        for y in x:
            lista_pcinco.append(y)  
            
    emocion_promedio_pcinco = mode(lista)

    print(f'Usuario: {lista_emociones.usuario} - {lista_emociones.actividad}: Primeros cinco minutos = {emocion_promedio_pcinco}')

obtener_reporte_emociones()