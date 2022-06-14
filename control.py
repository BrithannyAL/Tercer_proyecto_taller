from sonido import sonido
import os, io
from tkinter import messagebox
from proyecto3 import rostro

#Para los angulos del rostro
def detectar_concentracion():
    """
        Función que detecta los angulos del rostro para saber si el usuaruo está distraido."""
    
    from google.cloud import vision
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']= r'key.json'
    client=vision.ImageAnnotatorClient()

    with io.open('foto.png','rb') as image_file:
        content = image_file.read()
        
    image = vision.Image(content=content)
    response = client.face_detection(image=image)
    faces = response.face_annotations
    
    if faces:
        for face in faces:
            #dicccionario con los angulos asociados a la detección de la cara
            face_angles=dict(roll_angle=face.roll_angle,pan_angle=face.pan_angle,tilt_angle=face.tilt_angle)
            if  (face_angles['tilt_angle'] > 13) or (face_angles['tilt_angle'] < -15):
                sonido()
            elif (face_angles['pan_angle'] > 15) or (face_angles['pan_angle'] < -10):
                sonido()
    else:
        print('Ningún rostro fue detectado')
        
        
#Para las emociones
def analizar_emociones(face_expressions):
    expression_face = []
    
    for x in face_expressions:
        if ((face_expressions[x] in 'POSSIBLE') or
            (face_expressions[x] in 'LIKELY') or
            (face_expressions[x] in 'VERY_LIKELY')):
            expression_face.append(x)
    print(expression_face)
    
    for y in range(len(expression_face)):
        if expression_face[y] in 'joy_likelihood':
            expression_face[y] = 'Feliz'
        elif expression_face[y] in 'sorrow_likelihood':
            expression_face[y] = 'Triste'
        elif expression_face[y] in 'anger_likelihood':
            expression_face[y] = 'Enfadado'
        elif expression_face[y] in 'surprise_likelihood':
            expression_face[y] = 'Sorprendido'
        elif expression_face[y] in 'blurred_likelihood':
            expression_face[y] = 'Confundido'
            
    print(f'Sus emociones son {expression_face}')
    return expression_face
        
def detectar_emociones():
    from google.cloud import vision
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']= r'key.json'
    client=vision.ImageAnnotatorClient()

    with io.open('foto.png','rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.face_detection(image=image)
    faces = response.face_annotations
    
                     #desconocido #muy improbable #improbale  #posible   #probable  #muy probale
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE', 'LIKELY', 'VERY_LIKELY')

    if faces:
        for face in faces:
            #Probabilidad de Expresiones
            #Emociones: Alegría, tristeza, enfado, sorpresa, subexpuesto, confundido, ¿? 
            face_expressions=dict(  joy_likelihood=likelihood_name[face.joy_likelihood],
                                    sorrow_likelihood=likelihood_name[face.sorrow_likelihood],
                                    anger_likelihood=likelihood_name[face.anger_likelihood],
                                    surprise_likelihood=likelihood_name[face.surprise_likelihood],
                                    under_exposed_likelihood=likelihood_name[face.under_exposed_likelihood],
                                    blurred_likelihood=likelihood_name[face.blurred_likelihood],
                                    headwear_likelihood=likelihood_name[face.headwear_likelihood])
            
            print(f"Expresiones {face_expressions}")
            return analizar_emociones(face_expressions)