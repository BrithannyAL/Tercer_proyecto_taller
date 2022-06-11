from sonido import sonido
import os, io


def detectar():
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
            print(f'Angulos de la cara {face_angles}')
            detectar(face_angles)
    else:
        print('No se detecta ningún rostro')    
        
    if  (face_angles['tilt_angle'] > 13) or (face_angles['tilt_angle'] < -15):
        sonido()
    elif (face_angles['pan_angle'] > 15) or (face_angles['pan_angle'] < -10):
        sonido()
        
